#You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.
#Your function will accept three arguments:
#The first and second argument should be numbers.
#The third argument should represent a sign indicating the operation to perform on these two numbers.
def calculator(x, y, op):
    if type(x)!=int or type(y)!=int:
        return "unknown value"
    elif op=="+":
        return x+y
    elif op=="-":
        return x-y
    elif op=="*":
        return x*y
    elif op=="/":
        return x/y
    return "unknown value"