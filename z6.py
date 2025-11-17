def prime_factors(n):
    if n == 1:
        return "(1)"
    
    factors = {}
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        divisor += 1
    
    result = ""
    for prime, power in sorted(factors.items()):
        if power == 1:
            result += f"({prime})"
        else:
            result += f"({prime}**{power})"
    
    return result

# Тесты
print(prime_factors(86240))
print(prime_factors(1))
print(prime_factors(13))
print(prime_factors(100))
print(prime_factors(36))