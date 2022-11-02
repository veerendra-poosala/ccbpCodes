#HollowFullPyramid_2

rows_n = int(input())

for i in range(1,rows_n+1):
    
    left_spaces = " "*(rows_n-i)
    if i == 1:
        first_row = str(i)
        print(left_spaces+first_row)
    elif i == rows_n:
        last_row =""
        for l in range(1,rows_n+1):
            last_row = last_row+str(l)+" "
        print(left_spaces+last_row)
    else:
        hollow_spaces = "  "*(i-2)
        start_range = 1
        end_range = i +1 
        for j in range(start_range,end_range):
            f_char = str(start_range)+" "
            l_char = str(j)
        middle_rows = left_spaces+f_char+hollow_spaces+l_char
        print(middle_rows)