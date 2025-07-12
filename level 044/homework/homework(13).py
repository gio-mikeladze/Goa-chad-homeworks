def even_to_n(n):
    list=[]
    for i in range(1,n):
        if i%2==0:
            list.append(i)
    print(list)
even_to_n(8)