def binarize(M, threshold=0.5):
    result = []
    for row in M:
        new_row = []
        for value in row:
            if value > threshold:
                new_row.append(1)
            else:
                new_row.append(0)
        result.append(new_row)
    return result

# Тесты
print(binarize([[0.1, 0.6], [0.4, 0.9]], 0.5))
print(binarize([[0.1, 0.2, 0.3]], 0.25))
print(binarize([[1.0, 0.0], [0.5, 0.5]]))
print(binarize([[0.7]], 0.7))