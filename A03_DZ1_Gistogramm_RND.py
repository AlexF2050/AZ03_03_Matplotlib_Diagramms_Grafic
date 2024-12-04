import matplotlib.pyplot as plt
import numpy as np

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

# Добавление заголовка и подписей к осям
plt.title('Гистограмма случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')

# Отображение графика
plt.show()


