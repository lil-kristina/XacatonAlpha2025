from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import chat

app = FastAPI(title="Business Assistant", version="1.0.0")

# Раздаем статические файлы (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Разрешаем запросы от фронтенда - ИСПРАВЛЕННАЯ ВЕРСИЯ
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
)

app.include_router(chat.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Business Assistant API работает!"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Новый endpoint для главной страницы
@app.get("/app")
def serve_frontend():
    from fastapi.responses import HTMLResponse
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
