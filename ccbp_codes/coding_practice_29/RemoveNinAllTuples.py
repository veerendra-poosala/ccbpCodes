#RemoveNinAllTuples

num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]


n = int(input())

for i in range(len(num_list)):
    #converting into lists to remove the n from tuples
    num_list[i] = list(num_list[i])
    length = len(num_list[i])
    #print(length)
    for j in range(0,length):
        if num_list[i][j] == n:
            num_list[i].remove(n)
            break
    #print(num_list[i])

#converting back into tuples
for i in range(len(num_list)):
    num_list[i] = tuple(num_list[i])
print(num_list)

    

