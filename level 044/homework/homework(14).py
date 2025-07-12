def count_vowel(sentence):
    num=0
    for i in sentence.lower():
        if i=="a" or i=="e" or i=="o" or i=="u" or i=="i":
            num+=1
    print("in this sentence there is " +str(num)+" vowels")
count_vowel("GIORGI MIKELADZE")