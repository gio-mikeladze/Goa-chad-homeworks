number = int(input("Please enter a number: "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False

if is_prime:
    print("This is prime number")
else:
    print("This isn't prime number")