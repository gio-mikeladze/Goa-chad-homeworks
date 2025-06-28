#4) ასევე დაწერეთ პროგრამა, რომელიც შემოტანილ წინადადებას გადაიყვანს snake_case-ში.
sentence=input("Enter a sentence: ")
new=""
is_space=False
for i in sentence:
    if i==" ":
        is_space=True
    elif is_space:
        new=new+"_"+i
        is_space=False
    else:
        new=new+i
print(new)