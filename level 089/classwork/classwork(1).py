#Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with 
#a dash mark.

#Ex:

#274 -> '2-7-4'
#6815 -> '68-1-5'
def dashatize(n):
    result = []
    str_num = ""
    
    for i in (str(n) + "1").lstrip("-"):
        if int(i) % 2 == 0:
            str_num += i
        else:
            if str_num: result.append(str_num)
            result.append(i)
            str_num = ""
            
    return "-".join(result[:-1])