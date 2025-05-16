import numpy as np

# Создаем матрицу 5x5 со случайными целыми числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))

# Среднее значение всех элементов матрицы
mean_value = np.mean(matrix)

# Максимальное и минимальное значения во всей матрице
max_value = np.max(matrix)
min_value = np.min(matrix)

# Сумма по каждому столбцу
sum_columns = np.sum(matrix, axis=0)

# Вывод результатов
print("Матрица:")
print(matrix)
print("\nСреднее значение:", mean_value)
print("Максимальный элемент:", max_value)
print("Минимальный элемент:", min_value)
print("Суммы по столбцам:", sum_columns)