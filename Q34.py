def count_case(text):
    upper = sum(ch.isupper() for ch in text)
    lower = sum(ch.islower() for ch in text)
    return upper, lower

s = input("Enter string: ")
print("Uppercase, lowercase:", count_case(s))
