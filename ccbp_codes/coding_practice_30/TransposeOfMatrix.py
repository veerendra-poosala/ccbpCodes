#TransposeOfMatrix

def get_transpose_of_matrix(matrix,transpose_matrix = [],count = 0, m=0, n=0):
    
    row_matrix = matrix
    count = count
    transpose_of_matrix = transpose_matrix
    each_row = []
    n = n #no of cols
    
    for i in range(len(row_matrix)):
        for j in range(len(row_matrix[i])):
            if count == j:
                each_row += [row_matrix[i][j]]
                
    transpose_of_matrix += [each_row]
    if count == n - 1: #checking with cols value
        return transpose_of_matrix
    
    return get_transpose_of_matrix(row_matrix,transpose_matrix = transpose_of_matrix,count = count+1,n=n)
    

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

# Call the get_transpose_of_matrix function
reuslt = get_transpose_of_matrix(matrix = num_list,m=m,n=n)
for res in reuslt:
    print(res)