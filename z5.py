def mse(vector1, vector2):
    if len(vector1) != len(vector2):
        return "Векторы должны быть одинаковой длины"
    
    total = 0
    for i in range(len(vector1)):
        difference = vector1[i] - vector2[i]
        total += difference ** 2
    
    return total / len(vector1)

# Тесты
print(mse([1, 2, 3], [1, 2, 3]))
print(mse([1, 2, 3], [4, 5, 6]))
print(mse([0, 0, 0], [1, 1, 1]))
print(mse([2, 4, 6], [1, 3, 5]))