#list_rotation

#list = [1,2,3,4,5]
def rotate_list(int_list,rotate_times):
    first_list = int_list
    r = rotate_times
    r = r % len(first_list)
    r_list = []
    for i in range(r):
        item = first_list.pop(0)
        r_list.append(item)
    first_list.extend(r_list)
    
    return first_list

#method_2 
def rotate_list_method_2(int_list,rotate_times):
    
    r = rotate_times
    r = r % len(int_list)  
    first_list = int_list[:r]
    second_list = int_list[r:]
    second_list.extend(first_list)
    
    return second_list


int_list = list(map(int,input().split(",")))
rotate_times = int(input())

result = rotate_list_method_2(int_list,rotate_times)

print(result)