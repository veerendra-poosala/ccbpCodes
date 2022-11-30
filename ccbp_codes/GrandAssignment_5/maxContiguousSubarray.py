#maxContiguousSubarray
def get_sub_arrays_list(given_int_list, res_result=[], ref_pos=0, counter = 0):
    if len(given_int_list) == 1:
        return given_int_list
    #given_list
    given_int_list = given_int_list
    #required result list 
    new_list = res_result
    sub_array = []
    
    end = ref_pos
    c = 0
    while c < len(given_int_list):
        sub_list  =[]
        satrt = ref_pos
        if end == len(given_int_list):
            break
        for i in range(satrt, end+1):
            sub_list  += [given_int_list[i]]
        sub_array += [sub_list]
        end += 1
        c += 1

    new_list.append(sub_array)
    if counter == len(given_int_list) -1:
        return new_list
    return get_sub_arrays_list(given_int_list=given_int_list, res_result=new_list, ref_pos=ref_pos+1, counter = counter+1)

def get_max_val_sub_array(given_int_list):
    if len(given_int_list) <=1:
        return given_int_list
    max_sub_list = []
    max_value = sum(given_int_list[0][0])
    #iterating given list to find the maximum sum in sub arrays
    for items in given_int_list:
        for item in items:
            get_max = sum(item)
            if get_max > max_value:
                max_value = get_max
    #iterating again for getting sub array with total sum
    for items in given_int_list:
        for item in items:
            total = sum(item)
            if total == max_value:
                max_sub_list = item
                break
    return max_sub_list

def convert_int_list_string(int_list):
    result = ""
    for i in range(len(int_list)):
        char = str(int_list[i])
        result += char + " "
    return result

if __name__ == "__main__":
    #taking input as a int list 
    given_list = list(map(int,input().split()))
    #print(given_list)
    
    sub_arrays = get_sub_arrays_list(given_list)
    #print(sub_arrays)
    
    max_sub_array = get_max_val_sub_array(sub_arrays)
    #print(max_sub_array)
    result = convert_int_list_string(max_sub_array)
    print(result)