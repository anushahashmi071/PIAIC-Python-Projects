import math # For taking square root
a: int = int(input("Enter the length of side a: "))
b: int = int(input("Enter the length of side b: "))
c: int = math.sqrt(a ** 2 + b ** 2) # Calculate the hypotenuse using Pythagorean theorem
print(f"The length of the hypotenuse c is {c:.2f}")
