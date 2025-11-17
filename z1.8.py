def one_hot_encoding(labels):
    # Находим уникальные классы и сортируем их
    unique_classes = sorted(set(labels))
    # Создаем словарь для соответствия класса индексу
    class_to_index = {cls: idx for idx, cls in enumerate(unique_classes)}
    
    # Создаем one-hot encoding
    one_hot = []
    for label in labels:
        vector = [0] * len(unique_classes)
        vector[class_to_index[label]] = 1
        one_hot.append(vector)
    
    return one_hot

# Тесты
print("Тест 1:")
result1 = one_hot_encoding([0, 2, 3, 0])
for row in result1:
    print(row)

print("\nТест 2:")
result2 = one_hot_encoding([1, 0, 1, 2, 1])
for row in result2:
    print(row)

print("\nТест 3:")
result3 = one_hot_encoding([5, 2, 5, 2, 8])
for row in result3:
    print(row)