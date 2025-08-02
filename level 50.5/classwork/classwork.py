#I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.
#P.S. Each array includes only integer numbers. Output is a number too.
def array_plus_array(arr1,arr2):
    return sum(arr1)+sum(arr2)
#or

def array_plus_array(arr1,arr2):
    a=0
    b=0
    sum1=0
    sum2=0
    for i in range(0,len(arr1)):
        sum1=sum1+arr1[a]
        a+=1
    for k in range(0,len(arr2)):
        sum2=sum2+arr2[b]
        b+=1
    return sum1+sum2