#1) მომხმარებელს შემოატანინეთ ასაკი და შეამოწმეთ თუ ის ნაკლებია 18-ზე მაშინ შეამოწმეთ თუ ასაკი ნაკლებია 14-ზე დაუბეჭდეთ Discount 20%, 
# სხვა შემთხვევაში Discount 10%.
#თუ პირველი if-ი არასწორია დაბეჭდეთ No discount გამოიყენეთ ჩაშენებული if
age=int(input("Enter your age: "))
if age < 18:
    if age < 14:
        print("Discount 20%")
    else:
        print("Discount 10%")
else:
    print("No Discount")
#------------------------------------------------------------------------
#2) შექმენით infinity loop-ი(გამოიყენეთ while loop-ი)
num=1
while num<2:
    print(num)