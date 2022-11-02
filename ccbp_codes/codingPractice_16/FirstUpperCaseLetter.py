#FirstUpperCaseLetter

text = input()

for char in text:
    if char == char.upper() and char != char.lower():
        print(char)
        breakn