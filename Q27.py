def greatest(a, b, c):
    return max(a, b, c)

x, y, z = map(float, input("Enter three numbers: ").split())
print("Greatest:", greatest(x, y, z))
