#Write a function that takes a positive integer n, sums all the cubed values from 1 to n (inclusive), and returns that sum.
#Assume that the input n will always be a positive integer.
def sum_cubes(n):
    final=0
    for i in range(1,n+1):
        final+=i**3
    return final