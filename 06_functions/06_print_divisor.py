def is_divisor(num: int) -> int:
    for i in range(num):
        current_num: int = i + 1
        if num % current_num == 0:
            print(current_num)


def main():
    num = int(input("Enter a number: "))
    is_divisor(num)


main()
