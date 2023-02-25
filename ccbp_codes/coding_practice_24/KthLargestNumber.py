#KthLargestNumber



list_a = input().split(",")
position_k = int(input())
#print(list_a)
num_list = []
for char in list_a:
    char = int(char)
    num_list +=[char]
#print(num_list)
sorted_numlist = sorted(num_list,reverse = True)
index = position_k - 1
print(sorted_numlist[index])