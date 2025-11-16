import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from tokentelegram import token
from services.ai_service import ai_service

# Токен от BotFather
BOT_TOKEN = token

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    welcome_text = """
🤖 Привет! Я Бизнес-Помощник!

Я могу помочь с:
• Налогами и финансами
• Договорами и документами  
• Маркетингом и продажами
• Расчетами и аналитикой
• Управлением бизнесом
• Стартом нового дела

Просто задайте свой бизнес-вопрос!
    """
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    help_text = """
💡 Примеры вопросов:
• "Как рассчитать наценку?"
• "Какие налоги для ИП?"
• "Как составить договор?" 
• "Советы по маркетингу"
• "Как увеличить продажи?"
• "Что такое точка безубыточности?"
• "Как вести учет товара?"

Задайте любой бизнес-вопрос!
    """
    await update.message.reply_text(help_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений"""
    user_message = update.message.text
    
    # Показываем, что бот печатает
    await update.message.chat.send_action(action="typing")
    
    try:
        # Получаем ответ от AI сервиса
        answer = ai_service.get_ai_response(user_message)
        await update.message.reply_text(answer)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        await update.message.reply_text("❌ Произошла ошибка при обработке запроса. Попробуйте еще раз.")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик ошибок"""
    print(f"❌ Ошибка: {context.error}")
    
    # Безопасная отправка сообщения об ошибке
    try:
        if update and hasattr(update, 'message') and update.message:
            await update.message.reply_text("❌ Произошла ошибка, попробуйте позже")
        elif update and hasattr(update, 'callback_query') and update.callback_query:
            await update.callback_query.message.reply_text("❌ Произошла ошибка, попробуйте позже")
    except Exception as e:
        print(f"❌ Не удалось отправить сообщение об ошибке: {e}")

def main():
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Обработчик ошибок
    application.add_error_handler(error_handler)
    
    print("🤖 Telegram бот запущен...")
    print("⚠️  Если видите ошибки 'Conflict' - убедитесь, что запущен только один экземпляр бота")
    
    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
