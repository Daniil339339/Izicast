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
