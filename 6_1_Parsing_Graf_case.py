import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

# URL для парсинга
url = 'https://novosibirsk.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url) # Загрузка страницы

# Небольшая задержка для загрузки страниц
time.sleep(5)

# Список для хранения цен
prices = []

# Поиск элементов с ценами
price_elements = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

for price_element in price_elements:
    price = price_element.text
    prices.append(price)

# Сохранение цен в CSV файл
with open('price.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    for price in prices:
        writer.writerow([price])

# Завершение работы веб-драйвера
driver.quit()

print("Цены успешно сохранены в price.csv.")