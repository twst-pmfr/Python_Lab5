import numpy as np
import matplotlib.pyplot as plt

# Матрица 5x5 со случайными целыми числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))

# Тепловая карта с цветовой шкалой
plt.imshow(matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Значения')

# Добавляем аннотации внутри ячеек
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        text = plt.text(j, i, matrix[i][j], ha='center', va='center', color='w')

# Подписи осей и заголовок
plt.title('Тепловая карта случайных чисел')
plt.xlabel('Столбец')
plt.ylabel('Ряд')

# Показываем график
plt.show()