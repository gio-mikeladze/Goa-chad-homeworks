#7) შემქნით ცარიელი სია, სადაც 3-ჯერ input-ის სახით მომხმარებელს შეაყვანინებთ სამი სტუდენტის სახელს და დაამატებთ სიაში append() ფუნქციით.
# შემდეგ კი ჩასვით "Teacher" სიის თავში, წაშალეთ ბოლო სტუდენტი და დაბეჭდეთ სიის სიგრძე, ასვეე საბოლოო სია.

list=[]

for i in range(0,3):
    name=input("Enter students name: ")
    list.append(name)
list.insert(0,"Teacher")
list.pop()
print(len(list))
print(list)