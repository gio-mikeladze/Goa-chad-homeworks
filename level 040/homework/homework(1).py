#1) მომხმარებელს შემოატანინეთ წინადადება, დაითვალეთ მასში space-ების რაოდენობა და დაბეჭდეთ.
sentence=input("Enter a sentence: ")
num=0
for i in sentence:
    if i==" ":
        num += 1
print("we see spaces in this sentence "+str(num)+ " " + "times")