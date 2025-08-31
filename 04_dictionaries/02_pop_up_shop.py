fruits: dict = {}
while True:
    user_input: str = str(input(f"How many of each fruit they want to buy? "))
    if user_input == '':
        break
    fruits[user_input] = (input(f"Enter the quantity for {user_input}: "))
    quantity: int = int(fruits[user_input])

print(fruits)
