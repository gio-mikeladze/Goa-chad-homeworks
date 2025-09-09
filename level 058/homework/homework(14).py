#Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
#[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
#[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
#[] --> []
#You can assume that all values are integers. Do not mutate the input arra
def invert(lst):
    new_lst=[]
    for i in lst:
        if i>0:
            new_lst.append(-i)
        else:
            new_lst.append(-i)
    return new_lst