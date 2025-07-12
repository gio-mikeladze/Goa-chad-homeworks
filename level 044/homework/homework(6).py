def Arithmetic_mean(list):
    num=0
    number=0
    for i in list:
        num+=1
        number+=list[num-1]
    print(number/num)
Arithmetic_mean([5,67,65,43])