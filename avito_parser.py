import requests
from bs4 import BeautifulSoup
import time
from config import CHAT_ID, TELEGRAM_TOKEN
import telebot
from avito_keywords import KEYWORDS

bot = telebot.TeleBot(TELEGRAM_TOKEN)

URL = "https://www.avito.ru/sankt-peterburg?q="

already_sent = set()  # чтобы не слать одни и те же

def search_avito():
    for keyword in KEYWORDS:
        query_url = URL + requests.utils.quote(keyword)
        print(f"🔍 Ищем: {keyword}")
        response = requests.get(query_url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        # Ищем блоки объявлений
        for item in soup.select('a[data-marker="item-title"]'):
            title = item.text.strip()
            link = "https://www.avito.ru" + item["href"]

            if link not in already_sent:
                # Отправляем сообщение
                msg = f"🔎 Найдено по запросу *{keyword}*:\n[{title}]({link})"
                bot.send_message(CHAT_ID, msg, parse_mode="Markdown")
                already_sent.add(link)

def run_parser():
    while True:
        search_avito()
        time.sleep(600)  # каждые 10 минут
