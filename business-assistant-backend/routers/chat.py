from fastapi import APIRouter
from models import ChatRequest, ChatResponse
from services.ai_service import ai_service
from datetime import datetime

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    answer = await ai_service.get_ai_response(request.question)
    return ChatResponse(answer=answer, question=request.question, timestamp=datetime.now())
