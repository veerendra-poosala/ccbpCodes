#InvertedHalfPyramid_2

rows_n = int(input())
start_range = 1
i =1

for i in range(1,rows_n+1):
    result=""
    end_range = (rows_n+2)-i
    for j in range(start_range,end_range):
        star ="* "*j
        
    print(star)