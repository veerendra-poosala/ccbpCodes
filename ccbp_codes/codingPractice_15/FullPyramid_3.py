#FullPyramid_3

rows_n = int(input())

count = 1
for i in range(1,rows_n+1):
    
    zeros_pattern ="0 "*(rows_n-i)

    if i == 1:
        first_row = str(count)+" "
        print(zeros_pattern+first_row+zeros_pattern)
    
    elif i == rows_n:
        last_row ="1 "*count
        print(last_row)
    
    elif i > 1 and i < rows_n:
        middle_rows = "1 "*count
        print(zeros_pattern+middle_rows+zeros_pattern)
        
    count = count +2