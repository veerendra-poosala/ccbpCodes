
#MaxMinSumOfMatrix

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list

def find_max_min_sum(num_list):
    new_list = []
    for i in range(len(num_list)):
        for j in range(len(num_list[i])):
            new_list.append(num_list[i][j])
            
    new_list.sort()
    min_value = min(new_list)
    max_value = max(new_list)
    sum_value = sum(new_list)
        
    return max_value,min_value,sum_value


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

#print(num_list)

result = find_max_min_sum(num_list)

for num in result:
    print(num)

