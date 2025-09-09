#Your function takes two arguments:
#current father's age (years)
#current age of his son (years)
#Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
#The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
def twice_as_old(dad_years_old, son_years_old):
    n=0
    if son_years_old*2>=dad_years_old:
        while dad_years_old != son_years_old*2:
            n+=1
            son_years_old-=1
            dad_years_old-=1
        return n
    else:
        while dad_years_old != son_years_old*2:
            son_years_old+=1
            dad_years_old+=1
            n+=1
        return n