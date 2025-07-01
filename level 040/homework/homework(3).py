#3) გაკვეთილზე შევქმენით პროგრამა, რომელიც წინადადებას გადაიყვანს camelCase-ში. თქვენი დავალებაა დაწეროთ პროგრამა, რომელიც გააკეთებს 
#პირიქით. Input: "helloWorld" -> Output: "Hello world"

sentence=input("Enter a sentence in camelCAse: ")
new=""
for i in sentence:
    if i.upper()==i:
        new+=" "+i.lower()
    else:
        new+=i
print(new.capitalize())