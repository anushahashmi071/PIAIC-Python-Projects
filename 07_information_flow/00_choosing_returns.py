adult_age: int = 23


def is_adult(age: int):
    if age >= adult_age:
        return True
    elif age <= adult_age:
        return False


def main():
    age: int = int(input("How old is this person?: "))
    result = is_adult(age)
    print(result)


main()
