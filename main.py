import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
file_path = 'cleaned_Divan_price.csv'
data = pd.read_csv(file_path)

# столбец с ценами называется 'Цена'
prices = data['Цена']

# Вычисление средней цены
average_price = prices.mean()
print(f"Средняя цена: {average_price}")
# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Добавление средней цены на график
plt.axvline(average_price, color='r', linestyle='dashed', linewidth=2)

# Показать гистограмму
plt.show()





