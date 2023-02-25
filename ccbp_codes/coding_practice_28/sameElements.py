#SameElements

def convert_to_int_list(given_list):
    int_list = []
    for char in given_list:
        char = int(char)
        int_list += [char]
    return int_list

def same_elements(int_list):
    length = len(int_list)
    
    for num in int_list:
        count = int_list.count(num)
        if count == length:
            return True
        else:
            new_list = tuple(sorted(int_list))
            int_set = set(new_list) #for removing the duplicates
            new_int_list = list(int_set)
            new_int_list.sort() #for ascending order
            return new_int_list
    



#1)Taking the space separated integers from the user
given_list = input().split()
#print(given_list)

#2)convert_to_int_list
int_list = convert_to_int_list(given_list)
#print(int_list)

#3)check all are same elements in the list are not.
result = same_elements(int_list)
print(result)