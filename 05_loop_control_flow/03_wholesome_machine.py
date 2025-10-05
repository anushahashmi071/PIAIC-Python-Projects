affirmation: str = input("Enter an affirmation: ")
while True:
    print(f"Please type the following affirmation: {affirmation}")

    user_input: str = input()
    if user_input == affirmation:
        print("Correct affirmation")
        break
    else:
        print("Incorrect affirmation")
print("Done")
