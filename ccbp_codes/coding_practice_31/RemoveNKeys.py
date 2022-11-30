#RemoveNKeys

def remove_keys_from_dict(new_dict):
    
    #creating new dict with copy() method
    updated_dict = new_dict.copy()

    #getting inputs from user
    new_key_list = input().split()
    #print(new_key_list)

    for char in new_dict.keys():
        for item in new_key_list:
            if char == item:
                del updated_dict[char] #removing key from dict
    
    return updated_dict
    

alphabets = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
}

new_dict = remove_keys_from_dict(alphabets)
print(new_dict)
