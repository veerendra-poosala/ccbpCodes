#CombineTwoDictionaries

def add_two_dicts(dict_1,dict_2):
    
    #converting dicts items into lists
    dict_1_items_list = list(dict_1.items())
    dict_2_items_list = list(dict_2.items())
    
    #taking new list to concatenate above list items
    new_list = []
    
    length_dict_1 = len(dict_1_items_list)
    length_dict_2 = len(dict_2_items_list)
    
    #checking for greter length of dict
    if length_dict_1 > length_dict_2:
        length = length_dict_1
    else:
        length = length_dict_2
   
   #concatenating list items
    for i in range(length):
        if i < length_dict_1:
            new_list.append(dict_1_items_list[i])
        if i < length_dict_2:
            new_list.append(dict_2_items_list[i])
    
    #sorting in a ascending order   
    new_list.sort()
    #converting back to dicts to remove the duplicate keys
    result_dict = dict(new_list)
    result_list = list(result_dict.items())
    
    return result_list


def create_dict():
    new_dict = {}
    #taking space separated inputs from user
    keys_list = input().split() #keys
    vals_list = input().split() #values
    #print(keys_list)
    #print(vals_list)
    length = len(keys_list)
    
    for i in range(length):
        new_dict[keys_list[i]] = int(vals_list[i])
    
    return new_dict

dict_1 = create_dict()
dict_2 = create_dict()

sum_of_two_dicts = add_two_dicts(dict_1,dict_2)
print(sum_of_two_dicts)
