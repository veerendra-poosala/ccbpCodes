#NumberOfLowercaseAndUppercaseLetters

def count_of_lowercase_and_uppercase_letters(arg_1):
    upper_count = 0
    lower_count = 0
    for i in range(len(arg_1)):
        is_upper = arg_1[i] == arg_1[i].upper()
        is_lower = arg_1[i] == arg_1[i].lower()
        if is_upper and not(is_lower):
            upper_count += 1 
        elif is_lower and not(is_upper):
            lower_count += 1
            

    print(upper_count)
    print(lower_count)


word = input()
# Call the count_of_lowercase_and_uppercase_letters function
count_of_lowercase_and_uppercase_letters(word)

