#ShiftNumbers

#Move numbers to the end of the given string 

def shift_nums_to_end(given_string):
    
    digits = ''
    alpha_chars = ''
    resultant_string = ''
    
    for char in given_string:
        is_upper = char == char.upper() and not(char == char.lower())
        is_lower = char == char.lower() and not(char == char.upper())
        
        if char.isdigit():
            digits += char
        elif is_upper == True:
            alpha_chars += char
        elif is_lower == True:
            alpha_chars += char
    
    resultant_string = alpha_chars + digits
    return resultant_string
    


given_string = input()

resultant_string = shift_nums_to_end(given_string)
print(resultant_string)