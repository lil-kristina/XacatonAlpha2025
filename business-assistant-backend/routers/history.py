# routers/history.py
from fastapi import APIRouter
from models import HistoryResponse
from database import get_db_connection

router = APIRouter()

@router.get("/history/{user_id}", response_model=list[HistoryResponse])
async def get_user_history(user_id: int, limit: int = 10):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, user_id, question, answer, created_at 
        FROM chat_history 
        WHERE user_id = ? 
        ORDER BY created_at DESC 
        LIMIT ?
    """, (user_id, limit))
    
    history = []
    for row in cursor.fetchall():
        history.append(HistoryResponse(
            id=row[0],
            user_id=row[1],
            question=row[2],
            answer=row[3],
            created_at=row[4]
        ))
    
    conn.close()
    return history
