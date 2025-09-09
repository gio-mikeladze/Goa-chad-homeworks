def clone_of_split(word):
    final=[]
    string=""
    n=input("Enter a symbol: ")
    for i in word:
        if i!=n:
            string+=i
        else:
            final.append(string)
            string=""
    final.append(string)
    return final
print(clone_of_split("My Name Is anton"))