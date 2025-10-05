# user_input : int = int(input("Enter numbers: "))
# even_num: list[int] = []

# def count_even(user_input: int) -> int:
#     for i in range(user_input):
#         if i % 2 == 0:
#             print(i)
#             even_num.append(i)
#     return len(even_num)

# print(f"Even numbers: {even_num}")

# count_even(user_input)
def count_even(lst):
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            continue  # Ignore invalid inputs and prompt again

    even_count = sum(1 for num in lst if num % 2 == 0)
    print(even_count)


def main():
    my_list = []
    count_even(my_list)
    print("Final list:", my_list)  # Optional: to see the populated list


main()
