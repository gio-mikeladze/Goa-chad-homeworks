#You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent 
#you met yesterday evening?
#Write a simple function to check if the string contains the word hallo in different languages.
#These are the languages of the possible people you met the night before:
def validate_hello(greetings):
    list = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for i in list:
        if i in greetings.lower():
            return True
    return False