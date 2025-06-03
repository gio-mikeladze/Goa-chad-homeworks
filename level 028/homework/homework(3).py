positive_number=0
negative_number=0
for i in range(5):
    num=int(input("Enter a number: "))
    if num>0:
        positive_number=positive_number+1
    elif num<0:
        negative_number=negative_number+1
print("Positive numbers count:" +str(positive_number))
print("Negative number count:" +str(negative_number))