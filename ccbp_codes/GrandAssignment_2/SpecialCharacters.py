#SpecialCharacters

string = input()

vowels_count = 0
consonants_count = 0 

for char in string:
    is_vowel = char == 'a' or char == "A" or char =="e" or char == "E" or char == "i" or char == "I" or char == "o" or char == "O" or char == "u" or char == "U"
    letter = char == char.lower()
    letter_2 = char ==  char.upper()
    is_special_char = letter and letter_2
    #print(is_special_char)
    
    if is_special_char == False:
        if is_vowel:
            vowels_count = vowels_count + 1 
            #print(vowels_count)
        else:
            consonants_count = consonants_count + 1 
            #print(consonants_count)

print(vowels_count)
print(consonants_count)