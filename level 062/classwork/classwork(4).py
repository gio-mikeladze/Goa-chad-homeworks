#Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.
#For example n = 3 result in:
def draw_stairs(n):
    word=""
    a=""
    for i in range(1,n+1):
        a+=" "
        word+="I\n"+a
    return word[:-1-n]