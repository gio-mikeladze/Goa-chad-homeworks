#Write a function which calculates the average of the numbers in a given array.
#Note: Empty arrays should return 0.
def find_average(numbers):
    num=0
    sum=0        
    if numbers==[]:
        return 0
    for i in range(0,len(numbers)):
        num+=1
        sum+=numbers[num-1]
    return sum/len(numbers)