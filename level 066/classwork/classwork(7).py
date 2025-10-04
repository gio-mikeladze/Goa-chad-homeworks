#You must implement a function that returns the difference between the largest and the smallest value in a given list / array (lst) received as the parameter.
def max_diff(lst):
    if lst==[] or lst==[lst[0]]:
        return 0
    n=0
    for i in lst:
        if i>n:
            n=i
    a=0
    for b in lst:
        if b<=n and b<a:
            a=b
    return n-a