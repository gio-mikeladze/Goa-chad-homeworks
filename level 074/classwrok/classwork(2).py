#Simple, given a string of words, return the length of the shortest word(s).
#String will never be empty and you do not need to account for different data types.
def find_short(s):
    list=s.split()
    b=len(s)
    for i in list:
        if len(i)<b:
            b=len(i)
    return b