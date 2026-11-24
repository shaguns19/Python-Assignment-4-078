# Create square_module.py in this same folder with:
# def square(n):
#     return n * n
#
# Then run this program after creating the module.
try:
    from square_module import square
    n = float(input("Enter number: "))
    print("Square:", square(n))
except ImportError:
    print("Create square_module.py with a square(n) function first.")
