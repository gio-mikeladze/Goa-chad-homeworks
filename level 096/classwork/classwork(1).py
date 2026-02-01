#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
def digitize(n):
    a=''
    final=[]
    for i in str(n)[::-1]:
        a+=i
    for z in a:
        final.append(int(z))
    return final