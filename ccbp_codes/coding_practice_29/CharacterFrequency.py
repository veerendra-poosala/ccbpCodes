#CharacterFrequency


def char_frequency(given_line):
    given_line = given_line.lower()
    
    unique_char_set = set(given_line)
    unique_char_set.discard(" ")
    unique_char_set = sorted(unique_char_set)
    #print(unique_char_list)
    for char in unique_char_set:
        msg = "{}: {}"
        print(msg.format(char,given_line.count(char)))





def char_frequency(given_line):
    given_line = given_line.lower()
    #print(given_line)

    #converting into list and eliminating special characters by using string methods
    char_list = []
    for char in given_line:
        condition = char == char.lower() and not(char == char.upper())
        if condition == True:
            char_list += [char]
    char_list.sort() #sorting by ascending order
    #print(char_list)
    
    #creating unique character list by converting into tuple then set to eliminate the duplicate characters
    char_set = tuple(char_list)
    char_set = set(char_set)
    #print(char_set)
    
    unique_char_list = list(char_set)
    unique_char_list.sort() #sorting by ascending order
    #print(unique_char_list)
    
    #printing characters frequency by using count method and format method
    for letter in unique_char_list:
        count = char_list.count(letter)
        msg = "{0}: {1}"
        print(msg.format(letter,count))
    


given_line = input()

char_frequency(given_line)


