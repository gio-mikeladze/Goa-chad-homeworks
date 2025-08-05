#Write a function that removes the spaces from the string, then return the resultant string.
def no_space(x):
    spaces=""
    final=""
    for i in x:
        if i==" ":
            spaces+=" "
        else:
            final+=i
    return final