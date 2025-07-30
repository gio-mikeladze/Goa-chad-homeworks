#Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
def grow(arr):
    num=0 
    final_num=1
    for i in range(0,len(arr)):
        num+=1
        final_num=final_num*arr[num-1]
    return final_num