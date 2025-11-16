import os
import sys
import subprocess
import webbrowser
import time

def start_backend():
    """Запускает бэкенд сервер"""
    print("🚀 Запускаем бэкенд сервер...")
    
    # Проверяем существование main.py
    if not os.path.exists("main.py"):
        print("❌ Файл main.py не найден!")
        return False
    
    try:
        # Запускаем сервер в отдельном процессе
        backend_process = subprocess.Popen(
            [sys.executable, "main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        print("⏳ Ждем запуск сервера...")
        time.sleep(3)  # Даем время на запуск
        
        # Проверяем, жив ли процесс
        if backend_process.poll() is None:
            print("✅ Бэкенд сервер запущен на http://localhost:8000")
            return backend_process
        else:
            stdout, stderr = backend_process.communicate()
            print(f"❌ Ошибка запуска бэкенда: {stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка при запуске бэкенда: {e}")
        return False

def open_frontend():
    """Открывает фронтенд в браузере"""
    frontend_path = os.path.abspath("frontend/index.html")
    
    if os.path.exists(frontend_path):
        print("🌐 Открываем фронтенд в браузере...")
        webbrowser.open(f"file://{frontend_path}")
        print("✅ Фронтенд открыт в браузере")
    else:
        print("❌ Файл frontend/index.html не найден!")

def main():
    """Основная функция запуска"""
    print("=" * 50)
    print("🤖 Business Assistant - Автозапуск")
    print("=" * 50)
    
    # Запускаем бэкенд
    backend_process = start_backend()
    
    if backend_process:
        # Открываем фронтенд
        open_frontend()
        
        print("\n🎯 Система запущена!")
        print("• Бэкенд: http://localhost:8000")
        print("• Фронтенд: frontend/index.html")
        print("• API: http://localhost:8000/api/v1/chat")
        print("\n⏹️  Для остановки нажмите Ctrl+C")
        
        try:
            # Ждем завершения процесса
            backend_process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Останавливаем сервер...")
            backend_process.terminate()
    else:
        print("\n❌ Не удалось запустить систему")
        print("Попробуйте сначала установить зависимости:")
        print("python install.py")

if __name__ == "__main__":
    main()
