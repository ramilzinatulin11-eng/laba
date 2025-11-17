def unique_rows(mat):
    result = []
    for row in mat:
        unique = []
        for item in row:
            if item not in unique:
                unique.append(item)
        result.append(unique)
    return result

def unique_columns(mat):
    if not mat:
        return []
    
    result = []
    for col in range(len(mat[0])):
        unique = []
        for row in range(len(mat)):
            item = mat[row][col]
            if item not in unique:
                unique.append(item)
        result.append(unique)
    return result

# Тесты для строк
print("Уникальные строки:")
print(unique_rows([[1, 2, 3], [1, 1, 2], [4, 4, 4]]))
print(unique_rows([[1, 2, 1], [3, 3, 3]]))

# Тесты для столбцов
print("Уникальные столбцы:")
print(unique_columns([[1, 2, 3], [1, 1, 2], [4, 4, 4]]))
print(unique_columns([[1, 2, 1], [3, 3, 3]]))