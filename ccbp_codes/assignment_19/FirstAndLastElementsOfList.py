#FirstAndLastElementsOfList
terms_n = int(input())

new_list = []

for i in range(terms_n):
    n = int(input())
    new_list += [n]

#print(new_list)
length = len(new_list)
list_1 = new_list[:2]
#print(list_1)
list_2 = new_list[(length-2) :]
#print(list_2)
result = list_1 + list_2
print(result)