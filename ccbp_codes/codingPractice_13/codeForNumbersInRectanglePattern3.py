#code for NumbersInRectanglePattern3

rows_m = int(input())
cols_n = int(input())
start_index = 1
end_index = cols_n 
for i in range(1,rows_m+1):
    result = ""
    for j in range(start_index,end_index+1):
        result = result +str(j)+" "
        start_index = j+1
        end_index = cols_n + j 
    print(result)