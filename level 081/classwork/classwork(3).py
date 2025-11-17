#You will get an array of numbers.
#Every preceding number is smaller than the one following it.
#Some numbers will be missing, for instance:

def find_missing_numbers(arr):
    final=[]        
    if arr==[]:
            return []
    for i in range(arr[0],arr[-1]):
        if i not in arr:
            final.append(i)
    return final