#NestedList

rows = int(input())
new_list = []
for i in range(rows):
    int_list = list(map(int,input().split()))
    new_list += [int_list]
    
print(new_list)