from database import get_db_connection, get_or_create_user, save_chat_history
    
def test_database():
    # Проверяем подключение
    conn = get_db_connection()
    if conn:
        print("✅ Подключение к БД успешно!")
        conn.close()
    else:
        print("❌ Ошибка подключения к БД")
        return
    
    # Тестируем создание пользователя
    user_id = get_or_create_user(123456, "test_user")
    if user_id:
        print(f"✅ Пользователь создан/найден: ID {user_id}")
        
        # Тестируем сохранение истории
        if save_chat_history(user_id, "Тестовый вопрос", "Тестовый ответ"):
            print("✅ История чата сохранена!")
        else:
            print("❌ Ошибка сохранения истории")
    else:
        print("❌ Ошибка создания пользователя")

if __name__ == "__main__":
    test_database()
