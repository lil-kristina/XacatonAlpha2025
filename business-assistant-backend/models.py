from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    question: str
    user_id: int

class ChatResponse(BaseModel):
    answer: str
    question: str
    timestamp: datetime
