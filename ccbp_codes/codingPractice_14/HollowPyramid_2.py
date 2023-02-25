#HollowPyramid_2

rows_n = int(input())

for i in range(1,rows_n+1):
    
    if i == 1:
        print(str(i)+" ")
    elif i == rows_n:
        last_row =""
        for k in range(1,rows_n+1):
            last_row=last_row+str(k)+" "
        print(last_row)
    else:
        hollow_spaces = "  "*(i-2)
        start_range = 1
        end_range = i +1
        for j in range(start_range,end_range):
            first_char = str(start_range)+" "
            last_char = str(j)
        middle_lines = first_char+hollow_spaces+last_char
        print(middle_lines)
            
    