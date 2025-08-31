list1: list = []
while True:
    user_input: str = input("Enter a value (or press Enter to finish): ")
    if not user_input:  # If the input is empty, break the loop
        break
    list1.append(user_input)
print(f"List: {list1}")
