def average(items):
    return sum(items) / len(items) if items else None

values = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Average:", average(values) if values else "No numbers entered")
