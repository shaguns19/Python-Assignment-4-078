value = "Global value"
def demo():
    value = "Local value"
    print("Inside function:", value)

demo()
print("Outside function:", value)
