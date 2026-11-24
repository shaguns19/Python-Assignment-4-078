def sum_product(a, b):
    return a + b, a * b

x, y = map(float, input("Enter two numbers: ").split())
s, p = sum_product(x, y)
print("Sum:", s, "Product:", p)
