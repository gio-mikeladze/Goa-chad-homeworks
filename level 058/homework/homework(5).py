def clone_of_join(list):
    final=""
    num=-1
    n=input("Enter a symbol: ")
    for i in list:
        num+=1
        final+=list[num] + (n)
    return final[:-len(n)]
print(clone_of_join(['hello','world']))