def get_first_element(first: list) -> str:
    return first[0]

a: list[str] = ["Python", "is", "fun!"]
print(f"List: {a} \n\"{get_first_element(a)}\" is the first parameter in the list")
