import pyodbc
from config import settings

def get_db_connection():
    try:
        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={settings.DB_SERVER};"
            f"DATABASE={settings.DB_NAME};"
            f"UID={settings.DB_USER};"
            f"PWD={settings.DB_PASSWORD};"
        )
        return pyodbc.connect(connection_string)
    except Exception as e:
        print(f"❌ Ошибка подключения к БД: {e}")
        return None
