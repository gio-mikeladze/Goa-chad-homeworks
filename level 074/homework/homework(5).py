#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. 
#The string can contain any char.
def xo(s):
    a=0
    n=0
    for i in s:
        if i=="o" or i=="O":
            a+=1
        elif i=="x" or i=="X":
            n+=1
    if a==n:
        return True
    return False