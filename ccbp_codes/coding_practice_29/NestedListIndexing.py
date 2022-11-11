#NestedListIndexing


num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]

element = int(input())
res = ""
for i in range(len(num_list)):
    for j in range(len(num_list[i])):
        condition = element == num_list[i][j]
        if condition == True:
            res = str(i)+" "+str(j)
            
print(res)
            
