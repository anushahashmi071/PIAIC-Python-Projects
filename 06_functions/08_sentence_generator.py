def make_sentence(word: str, part_of_speech: str) -> None:
    if part_of_speech == "noun":  # noun
        print(
            f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == "verb":  # verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == "adjective":  # adjective
        print(f"Looking out my window, the sky is big and {word}!")


def main():
    word: str = input("Please type a noun, verb, or adjective: ")
    part_of_speech: str = input(
        "Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: ")

    make_sentence(word, part_of_speech)


main()
