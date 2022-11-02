#HyphenateLetters

given_line = input()

result =given_line[0]
for char in range(1,len(given_line)):
    result+="-"+given_line[char]
print(result)