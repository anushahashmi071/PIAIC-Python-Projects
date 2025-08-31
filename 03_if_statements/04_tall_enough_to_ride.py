user_height: int = int(input("Enter your height: "))
min_height: int = 50
if user_height <= min_height:
    print(
        f"Your height is {user_height}. You're not tall enough to ride, but maybe next year!")
else:
    print(f"Your height is {user_height}. You're tall enough to ride!")
