# Create arithmetic_module.py in this folder containing the four functions.
# Then use this importing program.
try:
    import arithmetic_module as ar
    a, b = map(float, input("Enter two numbers: ").split())
    print("Addition:", ar.add(a, b))
    print("Subtraction:", ar.subtract(a, b))
    print("Multiplication:", ar.multiply(a, b))
    print("Division:", ar.divide(a, b))
except ImportError:
    print("Create arithmetic_module.py with add, subtract, multiply and divide functions.")
