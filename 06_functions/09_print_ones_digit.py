def ones_digit(num: int) -> int:
    print(f"{num % 10}")


def main():
    num: int = int(input("Enter a number: "))
    ones_digit(num)


main()
