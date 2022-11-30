#ListOfUniqueTuples

n = int(input())
num_list = []

for i in range(n):
    item = list(map(int,input().split()))
    #print(item)
    length = len(item)
    max_count = 0
    for j in range(length):
        count = item.count(item[j])
        #print("count",count,"value",item[j])
        if count > 1 :
            max_count = count
    if max_count < 2:
        num_list += [item]

print(num_list)