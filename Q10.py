import math
number = float(input("Enter a number: "))
print("Ceiling:", math.ceil(number))
print("Floor:", math.floor(number))
if number >= 0:
    print("Square root:", math.sqrt(number))
else:
    print("Square root is not real for negative numbers.")
