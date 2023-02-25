#HollowInvertedHalfPyramid_2

rows_n = int(input())

for i in range(1,rows_n+1):
    
    if i == 1:
        first_row =""
        for k in range(1,rows_n+1):
            first_row = first_row+str(k)+" "
        print(first_row)
    elif i == rows_n:
        last_row = "1 "
        print(last_row)
    else:
        hollow_spaces = "  "*(rows_n-i-1)
        end_range=(rows_n+2)-i
        first_char = "1 "
        for j in range(1,end_range):
            last_char = str(j)    
        middle_rows = first_char+hollow_spaces+last_char
        print(middle_rows)
            