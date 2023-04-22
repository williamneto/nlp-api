from datetime import datetime

from fastapi import FastAPI, HTTPException
from mongoengine import connect

from schemas.completion import CompletionInput
from models.sessions import Session, SessionEntry, CompletionAnswer
from methods.completion import _complete

app = FastAPI()

@app.on_event("startup")
async def create_db_client():
    connect(
        "completion-api",
        host="localhost",
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

@app.post("/session/complete")
def complete(input: CompletionInput):
    session = Session.objects(
        id=input.session_id
    ).first()
    session_entry = SessionEntry(
        session=session,
        type=input.type,
        text=input.text
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
            full_prompt += "\n%s" % input.text
    else:
        full_prompt += "\n%s" % input.text
    
    completion_response = _complete(
        full_prompt
    )

    CompletionAnswer(
        input=session_entry,
        text=completion_response
    ).save()

    return completion_response