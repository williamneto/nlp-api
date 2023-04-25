from pydantic import BaseModel

from adapters.constants import DEFAULT_MODELS

class ClassificationInput(BaseModel):
    session_id: str
    prompt: str
    type: str = "in"
    model: str = ""