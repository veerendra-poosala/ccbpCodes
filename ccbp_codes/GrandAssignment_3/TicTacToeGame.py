#TicTacToeGame

#3*3 matrix
#abhinav = "O"
#anjali = "X"

def get_diagonal_matrix(game_data):
    diagonal_matrix = []
    row_1 = []
    for i in range(len(game_data)):
        for j in range(len(game_data[i])):
            if i == j:
                row_1 += [game_data[i][j]]
    diagonal_matrix.append(row_1)
    row_2 = []
    col_i = len(game_data[0])-1
    for row_i in range(len(game_data)):
        row_2 += [game_data[row_i][col_i]]
        col_i = col_i -1
    diagonal_matrix.append(row_2)
    
    return diagonal_matrix
                
    


def get_transpose_matrix(game_data=[],count = 0,transpose_matrix=[]):
    game_data = game_data
    new_matrix = transpose_matrix
    length = len(game_data[0]) #squre matrix so take rows or cols as length
    col_i = count
    row_list = []
    for row_i in range(length):
        row_list +=[game_data[row_i][col_i]]
        
    new_matrix += [row_list]
    
    if count >= length-1:
        return new_matrix
    return get_transpose_matrix(game_data=game_data,count=count+1,transpose_matrix=new_matrix)
    


def check_horizontal_lines(game_data):
    max_count = 0
    get_result = False
    length =len(game_data)
    msg = ''
    for i in range(length):
        count_o = 0
        count_x = 0
        for j in range(len(game_data[i])):
            char = game_data[i][j]
            #char = char.upper()
            if char == 'O':
                count_o += 1 
            elif char =='X':
                count_x += 1 
        
        if count_o == 3 and count_o > count_x:
            #print("count_o",count_o,"Abhinav Wins")
            get_result = True
            msg = "Abhinav Wins"
        elif count_x == 3 and count_x > count_o:
            #print("count_x",count_x,"Anjali Wins")
            get_result = True
            msg = "Anjali Wins"
        
    return msg,get_result
 

def check_matrix_data(game_data_list):
    game_data = game_data_list
    msg=''
    check_horizontally = check_horizontal_lines(game_data)
    #print(check_horizontally)
    transpose_of_game_data = get_transpose_matrix(game_data)
    #print(transpose_of_game_data)
    check_vertically = check_horizontal_lines(transpose_of_game_data)
    #print(check_vertically)
    diagonal_matrix = get_diagonal_matrix(game_data)
    #print(diagonal_matrix)
    check_diagonally = check_horizontal_lines(diagonal_matrix)
    #print(check_diagonally)
    
    if check_horizontally[1] == True:
        msg = check_horizontally[0]
        return msg
    elif check_vertically[1] == True:
        msg = check_vertically[0]
        return msg
    elif check_diagonally[1] == True:
        msg = check_diagonally[0]
        return msg
    else:
        msg = "Tie"
        return msg
    


def arrange_matrix(m):
    matrix = []
    for i in range(m):
        row = input().split()
        matrix.append(row)
    return matrix
        

m = 3 #given input as per problem
game_data_list = arrange_matrix(m)
check_data = check_matrix_data(game_data_list)
print(check_data)
