def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))   
print(count_vowels("world"))     
print(count_vowels("AEIOU"))     
print(count_vowels("python"))    
print(count_vowels(""))          