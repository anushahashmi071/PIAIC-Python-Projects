message: str = input("Enter a message for copying: ")
copy: list[str] = [message for _ in range(3)]
print(f"Copied message: {copy}")
