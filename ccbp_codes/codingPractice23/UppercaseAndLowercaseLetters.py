#UppercaseAndLowercaseLetters

def get_lower_and_upper_case_letters(word):
    upper_chars =''
    lower_chars =''
    for char in word:
        is_upper = char == char.upper()
        is_lower = char == char.lower()
        if is_upper and not(is_lower):
            upper_chars += char
        elif is_lower and not(is_upper):
            lower_chars += char
    print(upper_chars)
    print(lower_chars)
            


word = input()
get_lower_and_upper_case_letters(word)
