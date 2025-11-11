#Create a function that takes a number as an argument and returns a grade based on that number.
def grader(score):
    if score>1 or score<0.6:
        return "F"
    elif score>=0.9:
        return "A"
    elif score>=0.8:
        return "B"
    elif score>=0.7:
        return "C"
    return "D"