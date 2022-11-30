#matrixAssignmentAreaOfSquare

def find_small(val_1,val_2):
    Min = val_1
    if val_1 > val_2:
        Min = val_2
    return Min

def get_max(ver_mat,hor_mat,rows_m,cols_n):
    pass

    



def area_of_sub_matrix(matrix,rows_m,cols_n):
    
    Max = 0
    #creating auxilary matrices
    ver_mat = [[0 for i in range(cols_n)] for i in range(rows_m)]
    hor_mat = [[0 for i in range(cols_n)] for i in range(rows_m)]
    if matrix[0][0] == 'X':
        ver_mat[0][0] = 1
        hor_mat[0][0] = 1 
    #print(ver_mat,"\n",hor_mat)
    for i in range(rows_m):
        for j in range(cols_n):
            if matrix[i][j] == 'O':
                ver_mat[i][j],hor_mat[i][j] = 0,0
            else:
                if j == 0:
                    ver_mat[i][j],hor_mat[i][j] = 1,1 
                else:
                    ver_mat[i][j] = ver_mat[i-1][j] + 1
                    hor_mat[i][j] = hor_mat[i][j -1] + 1 
    
             
    for i in range((rows_m-1),0,-1):
        for j in range((cols_n-1),0,-1):
            small = find_small(ver_mat[i][j],hor_mat[i][j])
            
            while small > Max:
                if (ver_mat[i][j - small + 1] >= small and hor_mat[i - small + 1][j] >= small):
                    Max = small
                small -= 1
    return Max
                    

def get_matrix(rows_m,cols_n):
    matrix = []
    for i in range(rows_m):
        row = input().split()
        matrix.append(row)
    return matrix
        


rows_m,cols_n = map(int,input().split())
#print(rows_m,cols_n)
matrix = get_matrix(rows_m,cols_n)
#print(x_o_matrix)
sub_matrix = area_of_sub_matrix(matrix,rows_m,cols_n)
print(sub_matrix)
