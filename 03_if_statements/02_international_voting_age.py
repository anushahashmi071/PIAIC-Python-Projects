user_age: int = int(input("Enter your age: "))
voting_age_peturksbouipo: int = 16
voting_age_stanlau: int = 25
voting_age_mayengua: int = 48

if user_age > voting_age_mayengua:
    print(
        f"You are {user_age}. You are able to give vote in \"Peturksbouipo\", \"Stanlau\" and \"Mayengua\"")
elif user_age > voting_age_stanlau:
    print(f"You are {user_age}. You are able to give vote in \"Peturksbouipo\" and \"Stanlau\" and not able to give vote in \"Mayengua\"")
elif user_age > voting_age_peturksbouipo:
    print(f"You are {user_age}. You are able to give vote in \"Peturksbouipo\" and not able to give vote in \"Stanlau\" and \"Mayengua\"")
else:
    print(
        f"You are {user_age}. You are not able to give vote in \"Peturksbouipo\", \"Stanlau\" and \"Mayengua\"")
