#RenameKey

def update_dict_keys(dictionary,existing_key,new_key):
    new_dict = {}
    length = len(dictionary)
    
    for key,val in dictionary.items():
        if key == existing_key:
            new_dict[new_key] = val
            continue
        new_dict[key] = val
    
    new_list = list(new_dict.items())
    return new_list
    

fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}


existing_key = input()
new_key = input()

result = update_dict_keys(fruits,existing_key,new_key)
print(result)