#Create a function that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) and 
#consonants are in alternate order.
def is_alt(s):
    x = 0 if s[0] in "aeiou" else 1
    
    for i in range(len(s)):
        if i % 2 == x and s[i] not in "aeiou" or i % 2 != x and s[i] in "aeiou": return False
    return True