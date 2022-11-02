#HollowFullPyramid_1

rows_n = int(input())

for i in range(1,rows_n+1):
    
    left_spaces =" "*(rows_n-i)
    if i == 1:
        first_row = "* "*i
        print(left_spaces+first_row)
    elif i == rows_n:
        last_row ="* "*i 
        print(left_spaces+last_row)
    else:
        hollow_spaces = "  "*(i-2)
        print(left_spaces+"* "+hollow_spaces+"* ")