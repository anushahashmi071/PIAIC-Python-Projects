def get_number() -> list:
    count: list[int] = []
    while True:
        user_input = (input("Enter number: "))
        if user_input == "":
            break

        try:
            number = int(user_input)
            count.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer or press Enter to finish.")
            continue

    print("You entered:", count)
    return count

result = get_number()
print(result)