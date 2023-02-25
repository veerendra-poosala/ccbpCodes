#RotateDTimes

def rotate_list_d_times(int_list,rotate_times_d):
    
    length = len(int_list)
    rotate_times_d = rotate_times_d % length
    first_part = int_list[:rotate_times_d]
    second_part = int_list[rotate_times_d :]
    second_part.extend(first_part)
    
    return second_part
    
def rotate_list_d_times_method_2(int_list,rotate_times_d):
    first_list = int_list
    r = rotate_times_d
    r = r % len(first_list)
    r_list = []
    for i in range(r):
        item = first_list.pop(0)
        r_list.append(item)
    first_list.extend(r_list)
    
    return first_list

#getting comma-separated integers and rotate_times_d are inputs from user
int_list = list(map(int,input().split(",")))
rotate_times_d = int(input())

result = rotate_list_d_times_method_2(int_list,rotate_times_d)
print(result)


