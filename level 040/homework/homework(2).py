#2) შექმენით 5 ელემენტიანი სიტყვების სია. მომხმარებელს შემოატანინეთ სიტყვა და რიცხვი(ეს იქნება პოზიცია სადაც დაამატებთ შემოტანილ სიტყვას)
#დაბეჭდეთ განახლებული სია.
list_words=["Giorgi","Nika","Red banana","Apple","Water"]
word=input("Enter a word: ")
number=int(input("Enter a number (it is index where you want to put your word): "))
list_words.insert(number,word)
print(list_words)