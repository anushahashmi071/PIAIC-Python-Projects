def is_odd(num: int) -> bool:
    return num % 2 != 0


def main():
    num: int = int(input("Enter a number: "))
    if is_odd(num):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")


main()
