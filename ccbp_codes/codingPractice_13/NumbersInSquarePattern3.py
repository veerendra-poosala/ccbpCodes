#Numbers in Square Pattern - 3

rows_n = int(input())
start_index = 1
end_index = rows_n 
for i in range(1,rows_n+1):
    result = ""
    for j in range(start_index,end_index+1):
        result = result +str(j)+" "
        start_index = j+1
        end_index = rows_n + j 
    print(result)