#Complete the solution so that the function will break up camel casing, using a space between words.

#Example
#"camelCasing"  =>  "camel Casing"
#"identifier"   =>  "identifier"
#""             =>  ""
def solution(s):
    word=""
    list=[]
    for i in s:
        if i!=i.upper():
            word+=i
        else:
            list.append(word)
            word=i
    list.append(word)
    return " ".join(list)