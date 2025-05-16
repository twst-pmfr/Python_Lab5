import numpy as np
import matplotlib.pyplot as plt

# 1. Линейный график y = x^2
x = np.linspace(-5, 5, 100)  # Массив x от -5 до 5 с 100 точками
y = x**2                     # Значения y = x^2

# 2. Случайные точки для scatter-плотинга
points_x = np.random.randn(50) * 5  # 50 случайных точек
points_y = np.random.randn(50) * 5  # Координаты по обоим осям

# 3. Категории и соответствующие им значения для bar-диаграммы
categories = ['A', 'B', 'C']
values = [3, 7, 2]

# Создаем главную фигуру и три области subplots
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

# Первая область - линейный график
axes[0].plot(x, y, color='red')
axes[0].set_title('Квадратичная функция')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

# Вторая область - точечный график (scatter)
axes[1].scatter(points_x, points_y, color='green', marker='o')
axes[1].set_title('Точечный график')
axes[1].set_xlabel('X координата')
axes[1].set_ylabel('Y координата')

# Третья область - столбчатая диаграмма (bar)
axes[2].bar(categories, values, color=['orange', 'purple', 'cyan'])
axes[2].set_title('Категориальные данные')
axes[2].set_xlabel('Категория')
axes[2].set_ylabel('Значение')

# Настройка общей фигуры
plt.tight_layout()  # Убираем лишние отступы
plt.show()