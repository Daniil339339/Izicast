from threading import Thread
from avito_parser import run_parser  # подключаем парсер

# Запускаем парсер в отдельном потоке
Thread(target=run_parser, daemon=True).start()

# Ваш основной код для бота
import telebot
from config import TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Пример обработки команды /start
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я готов искать клиентов!")

bot.polling()
# bot.py
import telebot
from config import TELEGRAM_TOKEN, CHAT_ID

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def send_lead(text):
    bot.send_message(CHAT_ID, text)

# Тестовое сообщение
if __name__ == "__main__":
    test_message = "✅ Бот работает и готов к поиску клиентов!"
    send_lead(test_message)
