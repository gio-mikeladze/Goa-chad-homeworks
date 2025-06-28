#3) გაკვეთილზე შევქმენით პროგრამა, რომელიც წინადადებას გადაიყვანს camelCase-ში. თქვენი დავალებაა დაწეროთ პროგრამა, რომელიც გააკეთებს 
#პირიქით. Input: "helloWorld" -> Output: "Hello world"

sentence=input("Enter a sentence: ")
new=""
for i in sentence:
    if i.upper()==i:
        new=new+" "+i
    else:
        new+=i
print(new.capitalize())