#StringRotation

def rotate_list(str_list,ref_str,result_str):
    given_list = str_list
    length = len(given_list)
    counter = 0
    new_list = []
    while counter <= length:
        first_part = given_list[:(counter+1)]
        second_part = given_list[(counter+1):]
        new_list = second_part + first_part
        new_str = "".join(new_list)
        #print("new_str",new_str)
        base_condition = ref_str == result_str
        conditon = new_str == result_str 
        conditon_2 = counter > 1
        #print("new_str",new_str,"result_str",result_str,"counter",counter)
        if base_condition == True:
            return 0
        elif conditon and conditon_2:
            return  counter-1
        elif conditon and not(conditon_2):
            #print("counter",counter)
            return (length) - (counter+1)
    
        counter += 1
    
    return "No Match"  
    

def convert_str_to_list(ref_str):
    ref_string = ref_str

    #adding spaces to string then i will convert into list
    str_with_spaces = ''
    for char in ref_string:
        str_with_spaces += char + " "
    str_list = str_with_spaces.split()
    
    return str_list

s_1 = input()
s_2 = input()

str_list = convert_str_to_list(s_1) #actually there is no need to convert into list we can directly rotate the strings
rotations = rotate_list(str_list,s_1,s_2)
print(rotations)
