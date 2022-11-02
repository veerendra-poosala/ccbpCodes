#DoubleChar

given_line = input()

result =''

for char in given_line:
    char = char*2
    result += char
print(result)