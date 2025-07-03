#1) შექმენით ფუნქცია სახელად even_or_odd, რომელიც მომხმარებელს შემოატანინებს რიცხვს და დაბეჭდავს ლუწია თუ კენტია ის

def even_or_odd():
    num=int(input("Enter a number: "))
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
even_or_odd()

#2) შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს 5 სახელს. შექმნის მისგან სახელების სიას და დაბეჭდავს მას.

def names_lst():
    list_of_names=[]
    for i in range(5):
        list_of_names.append(input("Enter a name: "))
    print(list_of_names)
    
names_lst()

#3) შექმენი ფუნქცია, რომელიც მიიღებს რიცხვს და დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა რიცხვს.

def range_to_num(num):
   for i in range(1,num):
       print(i)

range_to_num(5)
range_to_num(12)
range_to_num(23)
range_to_num(50)
range_to_num(75)

#4) შექმენი ფუნქცია, რომელიც მიიღებს რიცხვს, და დაბეჭდავს რიგით მე-5 ლუწ რიცხვს შემოტანილი რიცხვის შემდეგ.

def number(num):
    if num%2==0:
        print(num+10)
    else:
        print(num+9)

number(5)
number(54)
number(15)
number(50)