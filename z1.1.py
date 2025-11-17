def sum_prod(X, V):
    total = 0
    for i in range(len(X)):
        matrix = X[i]
        vector = V[i]
        result = 0
        for j in range(len(matrix)):
            for k in range(len(vector)):
                result += matrix[j][k] * vector[k]
        total += result
    return total

# Тесты
print(sum_prod([[[1, 2], [3, 4]]], [[5, 6]]))
print(sum_prod([[[1, 0], [0, 1]]], [[1, 2]]))
print(sum_prod([[[1, 1], [1, 1]], [[2, 2], [2, 2]]], [[1, 1], [2, 2]]))
print(sum_prod([[[1]]], [[2]]))