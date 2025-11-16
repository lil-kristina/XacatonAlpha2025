import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_SERVER = os.getenv("DB_SERVER", "localhost")
    DB_NAME = os.getenv("DB_NAME", "business_assistant")
    DB_USER = os.getenv("DB_USER", "sa")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    
    # DeepSeek API настройки
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
    
    # Для совместимости
    YANDEX_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
    YANDEX_FOLDER_ID = ""

settings = Settings()
