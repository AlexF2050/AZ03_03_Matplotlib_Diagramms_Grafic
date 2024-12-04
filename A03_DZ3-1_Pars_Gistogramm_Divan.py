#Необходимо спарсить цены с сайта divan.ru

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.divan.ru/novosibirsk/category/odeala'
driver.get(url)
time.sleep(5)

products = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="product-card"]')
data = []
for product in products:
    price_element = product.find_element(By.CLASS_NAME, 'ui-LD-ZU')
    price = price_element.text
    data.append({'Цена': price})
driver.quit()
# Сохраняем данные в CSV файл
with open('Divan_price.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
print("Данные успешно сохранены в Divan_price.csv")