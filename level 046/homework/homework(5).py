def another_list(a_list):
    another_list=[]
    for i in a_list:
       another_list.insert(0,i)
    return another_list
print(another_list([5,6,7]))