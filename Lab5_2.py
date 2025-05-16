import numpy as np
import matplotlib.pyplot as plt

# Генерация 1000 случайных чисел с нормальным распределением
data = np.random.normal(loc=0, scale=1, size=1000)

# Построение гистограммы с 20 столбцами
plt.hist(data, bins=20, color="skyblue", edgecolor="black")

# Оформление графика
plt.title("Гистограмма случайных данных с нормальным распределением") # Заголовок
plt.xlabel("Значение")  # Ось X
plt.ylabel("Частота")    # Ось Y

# Показываем график
plt.show()