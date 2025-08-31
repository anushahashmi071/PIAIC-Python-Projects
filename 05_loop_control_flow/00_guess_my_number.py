import random

secret_number = random.randint(1, 99)

guess = int(input("Enter a number between 1 and 99: "))
while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Enter a number between 1 and 99: "))

print("Congratulations! You've guessed the number.")
