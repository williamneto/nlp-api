from pydantic import BaseModel

from adapters.constants import DEFAULT_MODELS

class CompletionInput(BaseModel):
    session_id: str
    prompt: str
    type: str = "in"
    use_history: bool = False
    model: str = DEFAULT_MODELS["text-generation"]