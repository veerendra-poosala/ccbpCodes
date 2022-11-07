#CommonElements

list_1 = list(map(int,input().split(",")))
list_2 = list(map(int,input().split(",")))

set_1 = set(list_1)
set_2 = set(list_2)

result = set_1.intersection(set_2)
result = list(result)
result.sort()

print(result)

#print(list_1)
#print(list_2)