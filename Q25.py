def string_length(text):
    count = 0
    for _ in text:
        count += 1
    return count

s = input("Enter string: ")
print("Length:", string_length(s))
