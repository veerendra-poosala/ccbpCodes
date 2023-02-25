list_a = input().split(",")
list_b = input().split(",")

len_of_list_a = len(list_a)
n = len_of_list_a - 1

for i in range(len_of_list_a):
    num_1 = list_a[i]
    num_2 = list_b[n-i]
    result = str(num_1) + " " + str(num_2)
    print(result)
