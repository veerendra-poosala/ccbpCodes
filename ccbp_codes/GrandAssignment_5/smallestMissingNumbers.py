#smallestMissingNumbers

def get_missing_num(missing_num_list):
    
    min_value = min(missing_num_list)
    missing_num = 0
    
    for i in range(len(missing_num_list)):
        item = missing_num_list[i]
        count = missing_num_list.count(item)
        #print("item", item ,"count",count)
        if count == 2 and i == 0:
            missing_num = min_value - 1
            break
        elif min_value != item:
                missing_num = min_value
                break
        min_value += 1
    return missing_num
        
    

given_list = list(map(int,input().split()))

ordered_list = sorted(given_list)
#print(ordered_list)
missing_num = get_missing_num(ordered_list)
print(missing_num)