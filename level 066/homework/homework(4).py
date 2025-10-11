#Write a function to split a string and convert it into an array of words.
def string_to_array(s):
    words=""
    final=[]
    for i in s:
        if i!=" ":
            words+=i
        elif i==" ":
            final.append(words)
            words=""
    final.append(words)
    return final