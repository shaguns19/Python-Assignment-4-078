counter = 10
def change_counter():
    global counter
    counter = 25

print("Before:", counter)
change_counter()
print("After:", counter)
