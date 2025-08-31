dividend: int = int(input("Enter a number to divide by: "))
divisor: int = int(input("Enter a number to divide: "))
qoutient: int = dividend // divisor  # Integer division
remainder: int = dividend % divisor  # Remainder of the division
print(f"The quotient is {qoutient} and the remainder is {remainder}.")
