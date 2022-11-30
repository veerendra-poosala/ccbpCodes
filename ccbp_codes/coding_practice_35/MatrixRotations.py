#MatrixRotations
from copy import deepcopy

def rotate_matrix(matrix,rotations=0):
    r_matrix = matrix
    #print("matrix",r)
    l = len(r_matrix) #length
    
    for i in range(l//2):
        for j in range(i,(l-i-1)):
            temp = r_matrix[i][j]
            #By using list mutability property,i'm updating r_matrix values
            r_matrix[i][j] = r_matrix[l-i-1][j]
            r_matrix[l-i-1][j] = r_matrix[l-i-1][l-j-1]
            r_matrix[l-i-1][l-j-1] = r_matrix[i][l-j-1]
            r_matrix[i][l-j-1] = temp 
    if rotations == 0:
        return r_matrix
    return rotate_matrix(r_matrix,rotations=rotations-1)

def get_matrix(n):
    int_matrix = []
    for i in range(n):
        row = list(map(int,input().split()))
        int_matrix = int_matrix+ [row]
    return int_matrix



if __name__ =="__main__":
    #taking inputs from user
    n = int(input())
    
    #given matrix
    int_matrix = get_matrix(n)
    
    #performing operatons
    #storing original list as dict keys
    ref_matrix = deepcopy(int_matrix) #shallow copying
    #print("ref_matrix",ref_matrix)
    run = True
    total_rotated_angle = 0
    while run:
        org_matrix = int_matrix[:]
        update_list  = []
        ops_list = input().split()
        #print(ops_list)
        if ops_list[0] == "R":
            angle = int(ops_list[1])
            rotations = (angle // 90)-1
            #rotating matrix 
            new_list = rotate_matrix(org_matrix,rotations)
            total_rotated_angle += angle
        
        elif ops_list[0] == "U":
            #updating value of matrix at row index i and column index j
            i = int(ops_list[1])
            j = int(ops_list[2])
            val = int(ops_list[3])
            
            update_list =deepcopy(ref_matrix)
            update_list[i][j] = val
            
            #after updation we need to rotate matrix by sum of all angle degrees
            if total_rotated_angle > 90:
                rotations = (total_rotated_angle//90)-1 
                #rotating matrix 
                up_list = rotate_matrix(update_list,rotations)
                new_list = deepcopy(up_list)
        elif ops_list[0] == "Q":
            i = int(ops_list[1])
            j = int(ops_list[2])
            query_list = ref_matrix
            if total_rotated_angle > 80:
                query_list = new_list
            elif len(update_list) > 1:
                query_list = update_list
                
                
                
            item = query_list[i][j]
            print(item)
            
        #print(org_matrix)
        if len(ops_list) == 1:
            exit = int(ops_list[0])
            if exit == -1:
                run = False
    #print("ref_matrix",ref_matrix)
  