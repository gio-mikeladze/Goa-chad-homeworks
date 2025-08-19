#Write a function that checks if a given string (case insensitive) is a palindrome.
#A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.
def is_palindrome(s):
    num=len(s)
    result=""
    a=s.lower()
    for i in s:
        num-=1
        result+=a[num]
    if result==s.lower():
        return True
    return False