def get_first_element(last: list) -> str:
    return last[-1]


a: list[str] = ["Python", "is", "fun!"]
print(f"List: {a}\n\"{get_first_element(a)}\" is the last parameter in the list")
