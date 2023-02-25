#AntiDiagonals

#printing resultant list
def print_list(anti_diagonals_list):
    
    for i in range(len(anti_diagonals_list)):
        string = ''
        for j in range(len(anti_diagonals_list[i])):
            string += str(anti_diagonals_list[i][j])+" "
        print(string)
    

#creating anti diagonals list
def create_anti_diagonals_list(matrix=[],rows_m=0, cols_n=0, count =0,ref_pos=1,new_list=[]):
    given_matrix = matrix
    new_list_length = (rows_m + cols_n) - 1 
    count = count
    rows_m = rows_m
    cols_n = cols_n
    diagonal_row = []
    diagonal_rows_list = new_list
   
    row_inc = ref_pos
    
    #print("new_list_length",new_list_length)
    #print(rows_m,"rows_m")
    #print("count",count)
    
    half_length = round((new_list_length+1) / 2)
    row_i = 0
    col_i = 0
    
    if count == 0:
        counter = 0
        while counter < count+1:
            if row_i < rows_m and col_i < cols_n:
                diagonal_row +=[matrix[row_i][col_i]]
            counter += 1
        
    
    elif count >= 1 and count <= cols_n:
        col_i = count 
        #print("col_i",col_i)
        counter = 0
        while counter < half_length:
            if col_i > cols_n -1 :
                break
            elif col_i < 0 or row_i > rows_m-1 :
                break
            elif row_i < rows_m and col_i < cols_n:
                diagonal_row +=[matrix[row_i][col_i]]
            
                #print("above: ","count",count,"row_i",row_i,"col_i",col_i,"counter",counter,"half_length",half_length)
                row_i += 1 
                col_i -= 1 
            counter += 1 
            
    elif count > cols_n and count <= new_list_length : 
        col_i = cols_n - 1 
        row_i = ref_pos
        #print("col_i",col_i)
        counter = 0
        while counter < half_length:
            
            if col_i < 0 or row_i > rows_m-1 :
                break
            elif row_i < rows_m and col_i < cols_n:
                diagonal_row +=[matrix[row_i][col_i]]
            
                #print("below: ","count",count,"row_i",row_i,"col_i",col_i,"counter",counter,"half_length",half_length)
                row_i += 1 
                col_i -= 1 
            counter += 1 
        
        row_inc += 1
        #print(row_inc)
    

    diagonal_rows_list += [diagonal_row]
    
    if new_list_length == count:
        resultant_list = diagonal_rows_list 
        new_list = [] 
        for items in resultant_list:
            if len(items) != 0:
                new_list += [items]
            
        return new_list
    
    return create_anti_diagonals_list(matrix=given_matrix,rows_m=rows_m,cols_n=cols_n,count = count+1,ref_pos = row_inc,new_list=diagonal_rows_list)
        
        

#creating matrix with rows_m
def create_matrix(rows_m):
    matrix = []
    for i in range(rows_m):
        string_list = input().split()
        row_num_list = convert_str_to_int_list(string_list)
        matrix += [row_num_list]
    return matrix

#converting string list to int list 
def convert_str_to_int_list(string_list):
    num_list = []
    for char in string_list:
        num = int(char)
        num_list += [num]
    return num_list
    

m,n = input().split()
rows_m = int(m)
cols_n = int(n)

matrix = create_matrix(rows_m)
#print(matrix)
anti_diagonals_list = create_anti_diagonals_list(matrix,rows_m,cols_n)
#print(anti_diagonals_list)
print_result = print_list(anti_diagonals_list)