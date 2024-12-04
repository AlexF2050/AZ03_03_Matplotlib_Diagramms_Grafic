import matplotlib.pyplot as plt
import numpy as np

# Генерация двух наборов случайных данных
random_array1 = np.random.rand(5)  # массив из 5 случайных чисел
random_array2 = np.random.rand(5)  # массив из 5 случайных чисел

# Создание диаграммы рассеяния
plt.scatter(random_array1, random_array2)

# Добавление заголовка и подписей к осям
plt.title('Диаграмма рассеяния')
plt.xlabel('Набор 1')
plt.ylabel('Набор 2')

# Отображение графика
plt.show()



