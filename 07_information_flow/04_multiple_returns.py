def get_user_data():
    first_name: str = input("Enter your first name: ")
    last_name: str = input("Enter your last name: ")
    email_address: str = input("Enter your email address: ")

    return first_name, last_name, email_address


def main():
    print(f'Here is your information: {get_user_data()}')


main()
