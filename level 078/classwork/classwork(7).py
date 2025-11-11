#An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
#Note: anagrams are case insensitive
#Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
def is_anagram(test, original):
    final=""
    if len(test)!=len(original):
        return False
    else:
        for i in test.lower():
            if i in original.lower():
                final=True
            elif i not in original.lower():
                return False
            else:
                final=False
    return final