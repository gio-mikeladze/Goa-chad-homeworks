#1) შექმენით ფუნქცია, რომელიც იღებს სამ რიცხვს და აბრუნებს ამ რიცხვებს შორის ყველაზე დიდს.
def num(a,b,c):
    if c<a>b:
        return str(a)+" is the biggest"
    elif c<b>a:
        return str(b)+" is the biggest"
    return str(c)+" is the biggest"
print(num(5,10,15))

#2) შექმენით ფუნქცია, რომელიც მიიღებს სიტყვას და დააბრუნებს მისი ასოების რაოდენობას.
def len_of_word(word):
    return len(word)
print(len_of_word("anna"))

#3) შექმენით ფუნქცია, რომელიც მიიღებს რაღაც რიცხვს, ამის შემდეგ კი დააბრუნებს ამ რიცხვის კვადრატულ მნიშვნელობას.
def square(num):
    return num**2 #num*num
print(square(5))

#4) შექმენით ფუნქცია, რომელიც მიიღებს 3 რიცხვს, თქვენი დავალებაა დააბრუნოთ ამ სამი რიცხვის ნამრავლი.
def three_nums(a,b,c):
    return a*b*c
print(three_nums(1,2,3))

#5) შექმენით ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "დადებითია" თუ რიცხვი დადებითია, "უარყოფითია" თუ რიცხვი უარყოფითია 
#და "ნულია" თუ შესაბამისად რიცხვი ნულის ტოლია.
def define_number(num):
    if num>0:
        return "დადებითია"
    elif num<0:
        return "უარყოფითია"
    return "ნულია"
print(define_number(5))