def repeat_string(word: str, times: int) -> None:
    for _ in range(times):
        print(word)


def main():
    user_str: str = input("Enter word to multiply: ")
    user_num: int = int(
        input("How many times you want to multiply the word: "))
    repeat_string(user_str, user_num)


main()
