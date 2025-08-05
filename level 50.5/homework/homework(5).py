#Your goal is to write a function that removes the first and last characters of a string. You're given one parameter, the original string.
#Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.
def remove_char(s):
    final=""
    num=0
    for i in range(0,len(s)-2):
        num+=1
        final+=s[num]
    return final