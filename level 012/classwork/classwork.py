#1) მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში როგორც string-ი. შემდეგ დაბეჭდეთ მისი მონაცემთა ტიპი.
#შეუცვალეთ მას მონაცემთა ტიპი ჯერ integer-ად, შემდეგ float-ად და თითოეული გარდაქმნისას დაბეჭდეთ მისი მონაცემთა ტიპი.
number=input("enter a number: ")
print(type(number))
number=int(number)
print(type(number))
number=float(number)
print(type(number))