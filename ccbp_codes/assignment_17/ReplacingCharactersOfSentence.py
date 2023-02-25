#ReplacingCharactersOfSentence

given_string = input()


next_char = ""
for char in given_string:
    
    condition_for_special_char = (char == char.lower() and char == char.upper())
    
    if condition_for_special_char == False:
        unicode_of_char = ord(char)
        unicode_of_next_char = unicode_of_char + 1
        next_char = next_char + chr(unicode_of_next_char)
    else:
        next_char = next_char + " "
print(next_char)