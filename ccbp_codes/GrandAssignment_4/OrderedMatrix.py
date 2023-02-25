#OrderedMatrix

def print_matrix(ordered_matrix):
    for num in ordered_matrix:
        res = ''
        for n in num:
            char = str(n)
            res += char + " "
        print(res)



def arrang_matrix_in_order(list_a=[],m=0,n=0):
    new_list =[]
    ordered_matrix = []
    
    #taking the inputs and arranging in an ascending order
    for i in range(m):
        row_list = list(map(int,input().split()))
        new_list.extend(row_list)
    new_list.sort()
    
    #creating ordered matrix
    length = len(new_list)
    required_rows = m
    required_cols = n 
    counter = 0 
    row_i = 0
    while counter < required_rows:
        row = []
        for i in range(row_i,length):
            row += [new_list[i]]
            length_of_row = len(row)
            if length_of_row == required_cols:
                break
        row_i += required_cols
        ordered_matrix.append(row)
        counter += 1

    return ordered_matrix

m,n = input().split()
rows_m = int(m)
cols_n = int(n)

ordered_matrix = arrang_matrix_in_order(m=rows_m,n=cols_n)
#print(ordered_matrix)
result = print_matrix(ordered_matrix)