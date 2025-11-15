import pyodbc
from config import settings

def get_db_connection():
    try:
        # Для sa без пароля используем Trusted Connection
        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={settings.DB_SERVER};"
            f"DATABASE={settings.DB_NAME};"
            f"Trusted_Connection=yes;"
            f"TrustServerCertificate=yes;"
        )
        
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print(f"❌ Ошибка подключения к БД: {e}")
        return None

def get_or_create_user(telegram_id: int, username: str = None):
    conn = get_db_connection()
    if not conn:
        return None
        
    cursor = conn.cursor()
    
    # Ищем существующего пользователя
    cursor.execute("SELECT id FROM users WHERE telegram_id = ?", telegram_id)
    user = cursor.fetchone()
    
    if user:
        user_id = user[0]
    else:
        # Создаем нового пользователя
        cursor.execute(
            "INSERT INTO users (telegram_id, username) OUTPUT INSERTED.id VALUES (?, ?)",
            telegram_id, username
        )
        user_id = cursor.fetchone()[0]
        conn.commit()
    
    conn.close()
    return user_id

def save_chat_history(user_id: int, question: str, answer: str):
    conn = get_db_connection()
    if not conn:
        return False
        
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_history (user_id, question, answer) VALUES (?, ?, ?)",
        user_id, question, answer
    )
    conn.commit()
    conn.close()
    return True
