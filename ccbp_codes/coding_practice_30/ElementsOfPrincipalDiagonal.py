#ElementsOfPrincipalDiagonal

def get_principal_diagonal_elements(matrix, m, n):
    principal_diagonal_elements = []
    row_matrix = matrix

    for i in range(len(row_matrix)):
        for j in range(len(row_matrix[i])):
            if i == j:
                principal_diagonal_elements += [row_matrix[i][j]]
                
    return principal_diagonal_elements
    

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

result = get_principal_diagonal_elements(num_list,m,n)
print(result)
