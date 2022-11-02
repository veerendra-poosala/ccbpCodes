#HallowInvertedFullPyramid_1

rows_n = int(input())

for i in range(1,rows_n+1):
    
    left_spaces = " "*(i-1)
    if i == 1:
        first_row = "* "*rows_n
        print(left_spaces+first_row)
    elif i == rows_n:
        last_row = "* "*(rows_n+1-i)
        print(left_spaces+last_row)
    else:
        hollow_spaces = "  "*(rows_n-i-1) #double spaces
        middle_rows = "* "+hollow_spaces+"* "
        print(left_spaces+middle_rows)