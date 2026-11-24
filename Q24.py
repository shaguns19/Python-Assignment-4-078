def count_vowels(text):
    return sum(ch.lower() in "aeiou" for ch in text)

s = input("Enter string: ")
print("Vowels:", count_vowels(s))
