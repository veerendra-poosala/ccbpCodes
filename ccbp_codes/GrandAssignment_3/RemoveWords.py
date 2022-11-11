#RemoveWords

def remove_word(string_list,rm_word_length_k):
    new_list = []
    for char in string_list:
        length = len(char)
        if length != rm_word_length_k:
            new_list += [char]
    #print(new_list)
    result_string = " ".join(new_list)
    return result_string



given_string = input().split() #taken as list
rm_word_length_k = int(input())

result = remove_word(given_string,rm_word_length_k)
print(result)


    
