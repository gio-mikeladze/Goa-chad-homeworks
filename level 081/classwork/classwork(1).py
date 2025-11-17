#Your task is to return an output string that translates an input string s by replacing each character in s with 
#a number representing the number of times that character occurs in s and separating each number with the sep character(s).

def freq_seq(s, sep):
    final=""
    for i in s:
        final+=str(s.count(i))+str(sep)
    return final[:-1]