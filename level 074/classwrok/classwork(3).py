#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers 
#in the form of a phone number.
#Example
#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
def create_phone_number(n):
    list1=[]
    list2=[]
    list3=[]
    for i in n[0:3]:
        list1.append(str(i))
    for i in n[3:6]:
        list2.append(str(i))
    for i in n[6:10]:
        list3.append(str(i))
    return "(" + "".join(list1) + ") " + "".join(list2) + "-" + "".join(list3)