#k_sum_of_pairs


def get_unique_combinations(initial_list,n=0,unq_comb=[],counter = 0):
    
    items_list = list(range(len(initial_list)))
    items_list = sorted(items_list)
    
    combinations_1 = unq_comb
    if counter == 0:
        for item in items_list:
            combinations_1.append([item])
        if n <= 0:
            orginal_values_list = []
            for combination in combinations_1:
                values = []
                for item in combination:
                    values.append(initial_list[item])
                orginal_values_list.append(tuple(values))
            orginal_list = sorted(set(orginal_values_list))  
            return orginal_list
            
    combinations_2 = []
    for combination in combinations_1:
        for item in items_list:
            if item < combination[-1]:
                combinations_2.append(combination+[item])
    if n <= 1:
        orginal_values_list = []
        for combination in combinations_2:
            values = []
            for item in combination:
                values.append(initial_list[item])
            orginal_values_list.append(tuple(values))
        orginal_list = sorted(set(orginal_values_list))  
        return orginal_list
    
    return get_unique_combinations(initial_list,n=n-1,unq_comb=combinations_2,counter = counter+1)
            


initial_list = list(map(int,input().split()))
new_list = set(tuple(initial_list))
initial_list = list(new_list)
k = int(input())
#print("initial_list: ",initial_list,"\n","k: ",k)
length = len(initial_list)
res_list = []
counter  = 0 
for n in range(length):
    unique_combinations = get_unique_combinations(initial_list,n=n)
    for item in unique_combinations:
        i  =sum(item)
        if i == k:
            counter += 1
        #print(item,counter)
    res_list.append(unique_combinations)

print(counter)