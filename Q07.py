import math
number = int(input("Enter a non-negative integer: "))
if number >= 0:
    print("Factorial:", math.factorial(number))
else:
    print("Factorial is undefined for negative integers.")
