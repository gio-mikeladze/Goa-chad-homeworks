#1) მომხმარებელს შემოატანინეთ სახელი და დაბეჭდეთ ის uppercase-ში

name=input("enter your name: ")
print(name.upper())
#or
name=input("enter your name: ")
new_name=name.upper()
print(new_name)

#2) იგივე სახელი დაბეჭდეთ lowercase-ში

name=input("enter your name: ")
print(name.lower())
#or
name=input("enter your name: ")
new_name=name.lower()
print(new_name)

#3) იგივე სახელი დაბეჭდეთ ისე, რომ მისი პირველი ასო იყოს uppercase-ში დაწერილი, ხოლო დანარჩენი lowercase-ში

name=input("enter your name: ")
print(name.capitalize())
#or
name=input("enter your name: ")
new_name=name.capitalize()
print(new_name)

#4) შექმენით ცვლადი, სადაც შეინახავთ ნებისმიერ სიტყვას. მომხმარებელს შემოატანინეთ სიმბოლო, რომლის ინდექსიც უნდა იპოვოთ სთრინგში და 
#დუბეჭდოთ შემდეგი ფორმატით "a - 0"
#თუ მომხმარებელმა ჩაწერა ისეთი სიმბოლო, რომელიც არ არის სიტყვაში. დაუბეჭდეთ რომ "This symbol is not in word"

word="football"
symbol=input("Enter a symbol: ")
if word.find(symbol)!=-1:
    print(str(word[word.find(symbol)])+" - "+str(word.find(symbol)))
else:
    print("This symbol is not in word")