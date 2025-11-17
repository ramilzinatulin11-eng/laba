def is_balanced(n):
    digits = str(n)
    length = len(digits)
    
    if length <= 2:
        return True
    
    if length % 2 == 0:
        mid = length // 2
        left_sum = sum(int(d) for d in digits[:mid-1])
        right_sum = sum(int(d) for d in digits[mid+1:])
    else:
        mid = length // 2
        left_sum = sum(int(d) for d in digits[:mid])
        right_sum = sum(int(d) for d in digits[mid+1:])
    
    return left_sum == right_sum

# Тесты
print(is_balanced(12321))
print(is_balanced(123321))
print(is_balanced(12345))
print(is_balanced(11))
print(is_balanced(1234))
print(is_balanced(123456))