#AddingTwoMatrices

def add_two_matrices(first_matrix, second_matrix, m, n):
    a_matrix = first_matrix
    b_matrix = second_matrix
    sum_matrix = []
    rows = m 
    cols = n 
    
    for i in range(rows):
        row_of_sum_matrix = []
        for j in range(cols):
            item = a_matrix[i][j] + b_matrix[i][j]
            row_of_sum_matrix += [item]
        sum_matrix += [row_of_sum_matrix]
        
    return sum_matrix


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


def read_matrix_inputs(m):
    num_list = []
    for i in range(m):
        list_a = input().split()
        list_a = convert_string_to_int(list_a)
        num_list.append(list_a)
    return num_list


m, n = input().split()
m, n = int(m), int(n)

first_matrix = read_matrix_inputs(m)
second_matrix = read_matrix_inputs(m)

result = add_two_matrices(first_matrix,second_matrix,m,n)

for res in result:
    print(res)