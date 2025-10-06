def greet(name: str) -> str:
    print(f"Hey {name}!!!")


def main():
    name: str = input("Enter your name: ")
    greet(name)


main()
