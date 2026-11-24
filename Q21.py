def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

n = int(input("Enter integer: "))
print("Sum of digits:", digit_sum(n))
