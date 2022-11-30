#Squares

def creating_square_dict(n):
    square_dict = {}
    num_list = list(range(1,n+1))
    #print(num_list)
    
    for num in num_list:
        square = num * num 
        square_dict[num] = square
    return square_dict


n = int(input())

new_dict = creating_square_dict(n)
print(new_dict)