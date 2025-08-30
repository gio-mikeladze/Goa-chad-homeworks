#Complete the solution so that it reverses all of the words within the string passed in.
#Words are separated by exactly one space and there are no leading or trailing spaces.
def reverse_words(s):
    words = []
    
    string1 = ""
    
    for i in s + " ":
        if i != " ":
            string1 += i
        else:
            words.append(string1)
            string1 = ""
    
    for i in words[::-1]:
        string1 += i + " "
    return string1[:-1]