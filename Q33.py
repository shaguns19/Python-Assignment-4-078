def largest(items):
    return max(items)

values = list(map(float, input("Enter list values: ").split()))
print("Largest:", largest(values))
