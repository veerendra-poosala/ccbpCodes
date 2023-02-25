#kSumPairs

def k_sum_pairs(int_list,number_k):
    
    stop_index = len(int_list) - 1
    result_set = set()
    
    for cur_index in range(stop_index):
        num_1 = int_list[cur_index]
        num_2 = number_k - num_1
        remaining_list = int_list[cur_index:]
        if num_2 in remaining_list:
            new_elements = (num_1,num_2)
            new_sets = list(new_elements)
            new_sets = tuple(sorted(new_sets))
            result_set.add(new_sets)
            
    
    result_set = list(result_set)
    result_set = sorted(result_set)
    
    return result_set


def k_sum_pairs_method_2(list_num,k):
    set_1 = set()
    pairs = ()
    for i in list_num:
        for j in list_num:
            condition = i + j == k 
            
            if condition == True:
                pair = (i,j)
                sorted_pair = tuple(sorted(pair))
                #print("sorted_pair",sorted_pair)
                set_1.add(sorted_pair)
    set_1 = list(set_1)
    set_1.sort()
    
    return set_1



int_list = list(map(int,input().split(",")))
number_k = int(input())

result = k_sum_pairs_method_2(int_list,number_k)
#print(result)

for r in result:
    print(r)
