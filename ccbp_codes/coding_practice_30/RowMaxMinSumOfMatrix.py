#RowMaxMinSumOfMatrix


def print_max_min_sum_for_row_wise(num_list):
    
    matrix = num_list
    max_row = max_matrix(matrix)
    min_row = min_matrix(matrix)
    sum_of_matrix = sum_matrix(matrix)
    result_matrix = [max_row] + [min_row] + [sum_of_matrix]
    
    return result_matrix


#finding maximum values in a row
def max_matrix(matrix):
    row_matrix = matrix
     
    max_row = []
    for num in row_matrix:
        max_digit = max(num)
        max_row += [max_digit]
    return max_row
#finding minimum values in a row   
def min_matrix(matrix):
    row_matrix = matrix
    min_row = []
    for num in row_matrix:
        min_value = min(num)
        min_row += [min_value]
    return min_row

#finding sum of items
def sum_matrix(matrix):
    row_matrix = matrix 
    
    sum_of_row_items = []
    for num in row_matrix:
        sum = 0
        for n in num:
            sum += n 
        sum_of_row_items += [sum]  
    return sum_of_row_items

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

result = print_max_min_sum_for_row_wise(num_list)
for res in result:
    print(res)

