def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter integer: "))
print("Factorial:", factorial(n) if n >= 0 else "Undefined for negative numbers")
