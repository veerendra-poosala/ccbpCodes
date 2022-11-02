#HollowInvertedFullPyramid_2

rows_n = int(input())

for i in range(1,rows_n+1):
    
    left_spaces = " "*(i-1)
    if i == 1:
        first_row =""
        for f in range(1,rows_n+1):
            first_row =first_row+str(f)+" "
        print(left_spaces+first_row)
    elif i == rows_n:
        last_row = rows_n+1-i
        print(left_spaces+str(last_row))
    else:
        hollow_spaces = "  "*(rows_n-i-1)
        start_range =1 
        end_range = rows_n+2-i
        for m in range(start_range,end_range):
            f_char = str(start_range)+" "
            l_char = str(m)
        middle_lines = left_spaces+f_char+hollow_spaces+l_char
        print(middle_lines)