#StudentIDMap

def print_key_val_of_dict(name_id_dict):
    dict_items = sorted(name_id_dict.items()) #sorting items to arrange ascending order
    for item in dict_items:
        print(*item)  #unpacking tuple
    
    
def mapping_data_dict(name_lsit,id_list):
    
    name_id_dict = {}
    names_lsit = (name_lsit)
    #print(names_lsit)
    ids_list = (id_list)
    
    length = len(names_lsit)
    
    for i in range(length):
        name_id_dict[names_lsit[i]] = ids_list[i]
   
    print_dict = print_key_val_of_dict(name_id_dict)    
    return print_dict
    


students_name_list = input().split(",")
students_id_list = input().split(",")

student_id_map = mapping_data_dict(students_name_list,students_id_list)
#print(student_id_map)