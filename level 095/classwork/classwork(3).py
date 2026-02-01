#Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
#Your task is to process a string with "#" symbols.
#Examples
#"abc#d##c"      ==>  "ac"
#"abc##d######"  ==>  ""
#"#######"       ==>  ""
#""              ==>  ""
def clean_string(s):
    list=[]
    n=0
    for i in s:
        if i!='#':
            list.append(i)
        elif i=="#" and len(list)!=0:
            list.pop(-1)
    return ''.join(list)