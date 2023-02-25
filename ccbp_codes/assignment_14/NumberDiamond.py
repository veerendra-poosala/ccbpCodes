#NumberDiamond

rows_n = int(input())

terms = (2*rows_n)-1 

for i in range(1,terms+1):
    left_spaces_upper = " "
    
    if i == 1:
        left_spaces_upper = " "*(rows_n-i)
        first_row = str(i)
        print(left_spaces_upper+first_row)

    elif i == int((terms+1) / 2):
        left_spaces_upper = " "*(rows_n-i)
        exact_middle_row = ""
        
        for e in range(1,rows_n+1):
            exact_middle_row = exact_middle_row+str(e)+" "
        print(left_spaces_upper+exact_middle_row)

    elif i == terms:
        left_spaces_lower = " "*(rows_n-1)
        last_row = "1 "
        print(left_spaces_lower+last_row)

    else:
        if i >1 and i < int((terms+1) / 2):
            left_spaces_upper = " "*(rows_n-i)
            start = 1 
            end = i + 1
            u_middle_rows = ""
            for j in range(start,end):
                u_middle_rows = u_middle_rows + str(j)+" "
            print(left_spaces_upper+u_middle_rows)
            
        elif i > int((terms+1) / 2) and i < (terms):
            left_spaces_lower = " "*(i - rows_n)
            start = 1 
            end = terms+2 - i
            l_middle_rows = ""
            for k in range(start,end):
                l_middle_rows = l_middle_rows + str(k)+" "
            print(left_spaces_lower+l_middle_rows)
        
            
        
            
        