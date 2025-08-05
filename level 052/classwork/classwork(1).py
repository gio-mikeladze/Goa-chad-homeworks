#You get an array of numbers, return the sum of all of the positives ones.
def positive_sum(arr):
    num=0
    final=0
    for i in arr:
        if i<0:
            num+=i
        else:
            final+=i
    return final