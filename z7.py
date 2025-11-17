def pyramid(n):
    total = 0
    k = 1
    
    while total < n:
        total += k * k
        if total == n:
            return k
        k += 1
    
    return "It is impossible"

# Тесты
print(pyramid(1))
print(pyramid(5))
print(pyramid(14))
print(pyramid(30))
print(pyramid(55))
print(pyramid(100))