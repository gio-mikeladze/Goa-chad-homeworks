#Write a function findNeedle() that takes an array full of junk but containing one "needle"
#After your function finds the needle it should return a message (as a string) that says:
#"found the needle at position " plus the index it found the needle, so:
def find_needle(haystack):
    n=0
    for i in haystack:
        if i!="needle":
            n+=1
        else:
            return "found the needle at position "+str(n)