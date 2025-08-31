def read_numbers():
    phonebook = {}
    while True:
        name: str = str(input("Enter name: "))

        if name == '':
            break
        number: int = int(input(f"Enter phone number for {name}: "))
        phonebook[name] = number
        if number == '':
            break
    return phonebook


phonebook = read_numbers()
print(phonebook)
