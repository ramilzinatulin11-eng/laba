def persistence(n):
    count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        count += 1
    return count

# Тесты
print(persistence(39))
print(persistence(4))
print(persistence(999))
print(persistence(25))
print(persistence(10))