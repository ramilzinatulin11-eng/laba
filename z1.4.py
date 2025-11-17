import random

def matrix_stats(m, n):
    # Создаем матрицу
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            # Генерируем случайное число из нормального распределения
            value = random.gauss(0, 1)
            row.append(round(value, 3))
        matrix.append(row)
    
    print("Матрица:")
    for row in matrix:
        print(row)
    
    # Мат ожидание и дисперсия для строк
    print("\n=== СТРОКИ ===")
    row_means = []
    row_vars = []
    
    for i in range(m):
        row = matrix[i]
        mean = sum(row) / len(row)
        variance = sum((x - mean) ** 2 for x in row) / len(row)
        row_means.append(round(mean, 3))
        row_vars.append(round(variance, 3))
        print(f"Строка {i+1}: мат.ожидание = {mean:.3f}, дисперсия = {variance:.3f}")
    
    # Мат ожидание и дисперсия для столбцов
    print("\n=== СТОЛБЦЫ ===")
    col_means = []
    col_vars = []
    
    for j in range(n):
        column = [matrix[i][j] for i in range(m)]
        mean = sum(column) / len(column)
        variance = sum((x - mean) ** 2 for x in column) / len(column)
        col_means.append(round(mean, 3))
        col_vars.append(round(variance, 3))
        print(f"Столбец {j+1}: мат.ожидание = {mean:.3f}, дисперсия = {variance:.3f}")
    
    return matrix

# Тест
result = matrix_stats(3, 4)