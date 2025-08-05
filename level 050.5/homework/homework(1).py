#Complete the solution so that it reverses the string passed into it.
#'world'  =>  'dlrow'
#'word'   =>  'drow'
def solution(string):
    final=""
    num=0
    for i in string:
        num+=-1
        final+=string[num]
    return final