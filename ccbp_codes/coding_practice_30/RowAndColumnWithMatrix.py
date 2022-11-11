#RowAndColumnWithMatrix

def find_row_and_col_elements_with_max(num_list,n = 0):
    n = n #no_of_cols 
    
    row_matrix = num_list
    row_matrix_max = find_max_val_row_in_col_matrix(row_matrix)
    
    col_matrix = row_into_col_matrix(num_list,n = n)
    col_matrix_max = find_max_val_row_in_col_matrix(col_matrix)
    
    return row_matrix_max,col_matrix_max


#finding max_value_row_in_col_matrix
def find_max_val_row_in_col_matrix(matrix = []):
    col_matrix = matrix
    #finding max value in col_matrix
    max_value_of_col_matrix = 0
    for num in col_matrix:
        max_value = max(num)
        if max_value_of_col_matrix <= max_value:
            max_value_of_col_matrix = max_value
    #print("max_value_of_col_matrix",max_value_of_col_matrix)
    
    for i in range(len(col_matrix)):
        max_value_of_row = max(col_matrix[i])
        if max_value_of_row == max_value_of_col_matrix:
            return col_matrix[i]
    
    
    
    
    
#converting into transpose matrix
#converting row elements into column elements and creating matrix with that elements
def row_into_col_matrix(num_list, count = 0, row_of_a_matrix = [], n=0 ):
    
    row_matrix = num_list
    col_matrix_row = []
    no_of_cols = n
    #print(no_of_cols)
    count = count
    full_col_matrix = row_of_a_matrix

    for i in range(len(row_matrix)):
        for j in range(len(row_matrix[i])):
            if count == j:
                col_matrix_row += [row_matrix[i][j]] #we can use append mehod also here
    
    full_col_matrix += [col_matrix_row]            
    if count == (no_of_cols - 1):
        return full_col_matrix
    
    
    #byusing recursion 
    return  row_into_col_matrix(row_matrix,count=count+1,row_of_a_matrix=full_col_matrix,n = no_of_cols )
    



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

result = find_row_and_col_elements_with_max(num_list,n=n)
for res in result:
    print(res)


