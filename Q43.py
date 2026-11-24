import math
n = int(input("Enter non-negative integer: "))
if n >= 0:
    print("Square root:", math.sqrt(n))
    print("Factorial:", math.factorial(n))
else:
    print("Please enter a non-negative integer.")
