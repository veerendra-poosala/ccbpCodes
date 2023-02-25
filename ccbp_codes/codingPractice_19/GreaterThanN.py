#GreaterThanN

num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
n = int(input())
list_new = []
for  i in num_list:
    if i > n:
        list_new += [i]
print(list_new)
    