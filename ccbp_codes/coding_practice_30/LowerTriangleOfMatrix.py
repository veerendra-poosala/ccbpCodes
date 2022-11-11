#LowerTriangleOfMatrix

def print_lower_triangle(matrix):
    lower_triangular_elements = []
    row_matrix = matrix

    for i in range(len(row_matrix)):
        each_row = []
        for j in range(len(row_matrix[i])):
            if i >= j:
                each_row += [row_matrix[i][j]]
        
        lower_triangular_elements += [each_row]
                
    return lower_triangular_elements

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

result = print_lower_triangle(num_list)
for res in result:
    print(res)
