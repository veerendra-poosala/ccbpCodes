#consecutive_sum_triangle

def sum_list_items(num_list):
    new_list = []
    length = len(num_list)
    
    for i in range(length -1): #iterating upto before last element
        num = num_list[i] + num_list[i+1]
        new_list.append(num)
    
    return new_list
 
 
def consecutive_sum_triangle(num_list):
    while len(num_list) >1 :
        next_list = sum_list_items(num_list)
        print(next_list)
        num_list = next_list



def convert_str_num_list(given_list):
    new_list = []
    for item in given_list:
        num = int(item)
        new_list.append(num)
    return new_list
    

given_list = input().split(",")
num_list = convert_str_num_list(given_list)
print(num_list)
sum_triangle = consecutive_sum_triangle(num_list)
