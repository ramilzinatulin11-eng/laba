def count_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1
    return count

# Тесты
print(count_bits(5))
print(count_bits(10))
print(count_bits(15))
print(count_bits(1))
print(count_bits(0))