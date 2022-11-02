#LargestNumberInList

list_a = input().split(",")
#print(list_a)
num_list = []
for char in list_a:
    char = int(char)
    num_list +=[char]
#print(num_list)
largest = max(num_list)
print(largest)