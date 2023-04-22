from pydantic import BaseModel

class CompletionInput(BaseModel):
    session_id: str
    text: str
    type: str = "in"
    use_history: bool = False