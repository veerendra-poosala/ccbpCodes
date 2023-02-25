#FirstWordInUpperCase

text_line = input()

for char in range(len(text_line)):
    if text_line[char] == " ":
        break 
    
first_word = text_line[:char].upper()
result = first_word + text_line[char:]
print(result)