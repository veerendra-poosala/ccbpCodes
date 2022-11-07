#ReplaceTheElement

num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]

num = int(input())
new_list = []
for item in num_list:
    
    item = list(item)
    item[-1] = num
    item = tuple(item)
    #print(item)
    new_list += (item,)
    #print(type(item))
print(new_list)



