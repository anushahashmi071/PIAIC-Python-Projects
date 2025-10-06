fahrenheit_temp: float = float(
    input("Enter a tempurature in Fahrenheit so it will be converted in Celsius: ")
)
print(f"Tempurture in Fahrenheit is {fahrenheit_temp} F")

celsius_temp: int = (fahrenheit_temp - 32) * 5 / 9
print(f"Tempurature in Celsius is {celsius_temp} C")
