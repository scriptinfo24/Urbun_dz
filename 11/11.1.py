
import numpy as np

# Создание массива чисел
array = np.array([1, 2, 3, 4, 5])

# Выполнение математических операций
sum_array = np.sum(array)
mean_array = np.mean(array)
std_array = np.std(array)

print(f"Сумма массива: {sum_array}")
print(f"Среднее значение массива: {mean_array}")
print(f"Стандартное отклонение массива: {std_array}")


import matplotlib.pyplot as plt

# Пример данных для визуализации
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Создание столбчатой диаграммы
plt.bar(categories, values)
plt.title('Пример столбчатой диаграммы')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.show()

