hidden_number=5
attempts=3
number_guessed=0
while hidden_number!=number_guessed and attempts>=0:
    number_guessed=int(input("Enter a number:"))
    if number_guessed!=hidden_number:
       print("wrong you have left guesses:" , (attempts))
    attempts=attempts-1
if hidden_number!=number_guessed:
    print("you lose")
else:
    print("you win")
