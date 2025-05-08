import requests
from bs4 import BeautifulSoup

# Ключевые слова для поиска
SEARCH_KEYWORDS = [
    "куплю сервировочные доски",
    "ищу доски для сервировки",
    "доски для подачи еды купить",
    "доска для сервировки в ресторане",
    "купить доски для подачи",
    "заказ доски для ресторанов",
    "сервировочная доска для кухни"
]

# Функция для поиска на Авито
def search_avito(keyword):
    # Замените URL на правильный, если используете авито
    base_url = "https://www.avito.ru"
    search_url = f"{base_url}/search?q={keyword}"

    # Запрос к сайту
    response = requests.get(search_url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Функция для обработки результатов поиска
def process_results(search_results):
    # Здесь можно добавить логику для обработки результатов
    # Например, извлечение информации из страницы
    soup = BeautifulSoup(search_results, 'html.parser')
    listings = soup.find_all('div', class_='iva-item-title')

    # Процесс обработки: например, печатаем заголовки найденных объявлений
    for listing in listings:
        title = listing.get_text()
        print(f"Найдено: {title}")

# Основная функция
def run_parser():
    for keyword in SEARCH_KEYWORDS:
        search_results = search_avito(keyword)
        if search_results:
            process_results(search_results)
        else:
            print(f"Ошибка при поиске для ключевого слова: {keyword}")

# Запуск парсера
if __name__ == "__main__":
    run_parser()
