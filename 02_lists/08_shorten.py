max_length: int = 3


def shorten_list(append_list):
    while len(append_list) > max_length:
        remove_item = append_list.pop()
        print(remove_item)


def main():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    shorten_list(lst)
    print(f"Final List: {lst}")


main()
