#5) შექმენით ცარიელი სია. მომხმარებელს შემოატანინეთ 5 სახელი და ჩაამატეთ ისინი ამ სიაში. გადაურეთ ამ სიას for ციკლით, შემდეგ კი 
# სახელის თითოეულ ასოს(დაგჭირდება 2 for ციკლით, ანუ for ციკლი მეორე for ციკლში). ასევე for ციკლების ზემოთ უნდა გქონდეთ შექმნილი კიდევ 
# ერთი ცარიელი სია, სადაც ჩაამატებთ ასოებიდან მხოლოდ თანხმოვნებს.
#გადაურეთ მიღებულ თანხმოვნების სიას და წაშალეთ დუბლიკატები, მოიძიეთ თუ როგორ შეიძლება სიის დასორტირება, დაასროტრირეთ ის ანბანის 
# მიხედვით და დაბეჭდეთ.
list=[]
other=[]
another_list=[]
for i in range(0,5):
    name=input("Enter a name: ")
    list.append(name)
for i in list:
    for z in i.lower():
        if z!="a" and z!="i" and z!="o" and z!="u" and z!="e":
            another_list.append(z)
for g in another_list:
    if g not in other:
        other.append(g)
other.sort()
print(other)