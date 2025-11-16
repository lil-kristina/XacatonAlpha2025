# routers/templates.py
from fastapi import APIRouter
from models import TemplateResponse
from database import get_db_connection

router = APIRouter()

@router.get("/templates", response_model=list[TemplateResponse])
async def get_templates(category: str = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if category:
        cursor.execute("SELECT id, name, category, content FROM templates WHERE category = ?", category)
    else:
        cursor.execute("SELECT id, name, category, content FROM templates")
    
    templates = []
    for row in cursor.fetchall():
        templates.append(TemplateResponse(
            id=row[0],
            name=row[1],
            category=row[2],
            content=row[3]
        ))
    
    conn.close()
    return templates

@router.get("/templates/{template_id}")
async def get_template(template_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, category, content FROM templates WHERE id = ?", template_id)
    row = cursor.fetchone()
    
    conn.close()
    
    if row:
        return TemplateResponse(
            id=template_id,
            name=row[0],
            category=row[1],
            content=row[2]
        )
    else:
        return {"error": "Template not found"}
