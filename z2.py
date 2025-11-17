def is_unique_chars(string):
    seen_chars = set()
    for char in string:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True

# Тесты
print(is_unique_chars("abcde"))
print(is_unique_chars("hello"))
print(is_unique_chars("12345"))
print(is_unique_chars("aabbcc"))
print(is_unique_chars(""))