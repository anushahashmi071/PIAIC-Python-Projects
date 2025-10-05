num1: int = int(input("Enter a number: "))
num2: int = int(input("Enter a number: "))


def average(num1: int, num2: int) -> int:
    return (num1 + num2) / 2


print(f"The average of {num1} and {num2} is {average(num1, num2)}")
