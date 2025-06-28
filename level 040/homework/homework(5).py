#5) შექმენით ცარიელი სია. მომხმარებელს შემოატანინეთ 5 სახელი და ჩაამატეთ ისინი ამ სიაში. გადაურეთ ამ სიას for ციკლით, შემდეგ კი 
# სახელის თითოეულ ასოს(დაგჭირდება 2 for ციკლით, ანუ for ციკლი მეორე for ციკლში). ასევე for ციკლების ზემოთ უნდა გქონდეთ შექმნილი კიდევ 
# ერთი ცარიელი სია, სადაც ჩაამატებთ ასოებიდან მხოლოდ თანხმოვნებს.
#გადაურეთ მიღებულ თანხმოვნების სიას და წაშალეთ დუბლიკატები, მოიძიეთ თუ როგორ შეიძლება სიის დასორტირება, დაასროტრირეთ ის ანბანის 
# მიხედვით და დაბეჭდეთ.
list=[]
num=0
another_list=[]
for i in range(0,5):
    name=input("Enter a name: ")
    list.append(name)
for i in list:
    for z in i:
        if z!="A" and z!="a" and z!="i" and z!="I" and z!="O" and z!="o" and z!="U" and z!="u" and z!="E" and z!="e":
            another_list.append(z)
for i in another_list:
    num+=1
    if another_list[num]==i:
        i=""
another_list.sort()
print(another_list)