def palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

s = input("Enter string: ")
print("Palindrome" if palindrome(s) else "Not palindrome")
