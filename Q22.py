def largest(items):
    return max(items)

values = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Largest:", largest(values))
