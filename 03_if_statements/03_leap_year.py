year: int = int(input("Enter a Year: "))
if (year % 4 and year % 100) or (year % 400 == 0):
    print(f"{year} is not a Leap Year")
else:
    print(f"{year} is a Leap Year")
