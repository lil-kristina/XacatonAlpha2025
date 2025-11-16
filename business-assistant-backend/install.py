import subprocess
import sys
import os

def run_command(command):
    """Выполняет команду и выводит результат"""
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✅ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка в команде: {command}")
        print(f"Ошибка: {e.stderr}")
        return False

def install_dependencies():
    """Устанавливает все необходимые зависимости"""
    print("🚀 Устанавливаем зависимости для Business Assistant...")
    
    # Список зависимостей
    dependencies = [
        "fastapi==0.104.1",
        "uvicorn==0.24.0", 
        "pyodbc==4.0.39",
        "python-dotenv==1.0.0",
        "aiohttp==3.9.1",
        "python-telegram-bot==20.7",
        "pydantic==2.5.0",
        "python-multipart==0.0.6",
        "requests==2.31.0"
    ]
    
    # Устанавливаем каждую зависимость
    for package in dependencies:
        command = f'"{sys.executable}" -m pip install {package}'
        if not run_command(command):
            print(f"⚠️ Пропускаем {package}, продолжаем установку...")
    
    print("🎉 Все зависимости установлены!")

def check_installation():
    """Проверяет успешность установки"""
    print("\n🔍 Проверяем установку...")
    
    packages_to_check = [
        "fastapi",
        "uvicorn", 
        "pyodbc",
        "aiohttp",
        "python_telegram_bot"
    ]
    
    for package in packages_to_check:
        try:
            if package == "python_telegram_bot":
                __import__("telegram")
            else:
                __import__(package)
            print(f"✅ {package} - OK")
        except ImportError as e:
            print(f"❌ {package} - НЕ УСТАНОВЛЕН: {e}")

def main():
    """Основная функция"""
    print("=" * 50)
    print("🤖 Business Assistant - Установщик зависимостей")
    print("=" * 50)
    
    # Устанавливаем зависимости
    install_dependencies()
    
    # Проверяем установку
    check_installation()
    
    print("\n🎯 Что дальше:")
    print("1. Запустите бэкенд: python main.py")
    print("2. Откройте frontend/index.html в браузере")
    print("3. Проверьте работу по адресу: http://localhost:8000")

if __name__ == "__main__":
    main()
