fruit_list: dict[str, int] = {
    "apple": 20,
    "mango": 10,
    "cherry": 30,
    "banana": 40
}


def num_in_stock(fruit: str) -> int:
    if fruit in fruit_list:
        return fruit_list[fruit]
    else:
        return 0


def main():
    fruit = input("Enter a Fruit: ")
    quantity = num_in_stock(fruit)

    if quantity > 0:
        print("This fruit is in stock! Here is how many:")
        print(quantity)
    else:
        print("This fruit is not in stock.")


main()
