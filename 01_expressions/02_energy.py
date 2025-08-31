mass: int = int(input("Enter your Mass in kg: "))
c: int = 299792458  # Speed of light in m/s
energy: int = mass * c ** 2

print(f"Your energy is {energy} in Joules")
