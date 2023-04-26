import os
from datetime import datetime
from typing import Annotated

from fastapi import FastAPI, HTTPException, Body
from mongoengine import connect

from schemas.completion import CompletionInput
from schemas.classification import ClassificationInput
from models.sessions import Session, SessionEntry, CompletionAnswer
from methods.completion import _complete
from methods.classification import _classify
from adapters.constants import DEFAULT_MODELS
from train import train_clm

app = FastAPI()

@app.on_event("startup")
async def create_db_client():
    connect(
        "completion-api",
        host=os.environ.get("dbname") or "localhost",
        port=27017,
        username="root",
        password="password"
    )

@app.get("/session/start")
def start_session():
    session = Session(
        started=datetime.now()
    ).save()

    return str(session.id)

@app.post("/session/classify")
def classify(input: ClassificationInput):
    session = Session.objects(
        id=input.session_id
    ).first()

    SessionEntry(
        session=session,
        operation="completion",
        type=input.type,
        text=input.prompt
    ).save()

    if not input.model:
        input.model = DEFAULT_MODELS["text-classification"]

    return _classify(
        input.prompt,
        model=input.model
    )

@app.post("/session/analyse_sentiment")
def analyse_sentiment(input: ClassificationInput):
    session = Session.objects(
        id=input.session_id
    ).first()

    SessionEntry(
        session=session,
        operation="completion",
        type=input.type,
        text=input.prompt
    ).save()

    if not input.model:
        input.model = DEFAULT_MODELS["sentiment-analisys"]

    return _classify(
        input.prompt,
        model=input.model
    )

@app.post("/session/complete")
def complete(input: CompletionInput):
    session = Session.objects(
        id=input.session_id
    ).first()
    session_entry = SessionEntry(
        session=session,
        operation="completion",
        type=input.type,
        text=input.prompt
    ).save()

    has_base_input = SessionEntry.objects(
        session=session,
        type="base"
    )

    base_input = ""
    if has_base_input:
        base_input = has_base_input.first()

    session_inputs = SessionEntry.objects(
        session=session,
        type="in"
    )

    full_prompt = base_input
    if input.use_history:
        for input in session_inputs:
            full_prompt += "\n%s" % input.prompt
    else:
        full_prompt += "\n%s" % input.prompt
    
    completion_response = _complete(
        full_prompt,
        model=input.model
    )[0]["generated_text"]

    CompletionAnswer(
        input=session_entry,
        text=completion_response
    ).save()

    return completion_response

@app.post("/train")
def train(
    data_training_args: train_clm.ModelDataTrainingArguments,
    output_dir: Annotated[str, Body()],
    do_train: Annotated[bool, Body()],
    do_eval: Annotated[bool, Body()],
    overwrite_output_dir: Annotated[bool, Body()]
):
    train_clm.train(
        data_training_args,
        output_dir,
        do_train,
        do_eval,
        overwrite_output_dir=overwrite_output_dir
    )