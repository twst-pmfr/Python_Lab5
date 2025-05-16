import numpy as np
import matplotlib.pyplot as plt

# Генерация массива x от 0 до 10 с 100 элементами
x = np.linspace(0, 10, 100)

# Вычисление значений функций синус и косинус
y = np.sin(x)
z = np.cos(x)

# Построение двух графиков на одной оси
plt.plot(x, y, label='sin(x)')
plt.plot(x, z, label='cos(x)')

# Добавляем легенду
plt.legend()

# Подписываем оси
plt.xlabel('X')
plt.ylabel('Y')

# Заголовок графика
plt.title('Графики функций синусов и косинусов')

# Отображаем график
plt.show()