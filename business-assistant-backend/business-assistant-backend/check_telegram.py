try:
    from telegram import Update
    from telegram.ext import Application
    print("✅ Библиотека telegram работает!")
except ImportError as e:
    print(f"❌ Ошибка: {e}")
