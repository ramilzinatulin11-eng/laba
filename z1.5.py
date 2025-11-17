def chess_matrix(m, n, a, b):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:
                row.append(a)
            else:
                row.append(b)
        matrix.append(row)
    return matrix

# Тесты
print("Тест 1 (2x2):")
for row in chess_matrix(2, 2, 1, 0):
    print(row)

print("\nТест 2 (3x3):")
for row in chess_matrix(3, 3, 'X', 'O'):
    print(row)

print("\nТест 3 (4x3):")
for row in chess_matrix(4, 3, 5, 10):
    print(row)