#1) მომხმარებელს შემოატანინეთ წინადადება და შეინახეთ ის ცვლადში. თქვენი დავალებაა ეს შემოტანილი წინადადება გადაიყვანოთ camelCase-ში.
#(ამ დავალების შესასრულებლად არ უნდა გამოიყენოთ .title ფუნქცია)
sentence=input("Enter a sentence: ")
result=""
is_space=False
for i in sentence.lower():
    if i == " ":
        is_space=True
    elif is_space:
        result += i.upper()
        is_space=False
    else:
        result += i
print(result)