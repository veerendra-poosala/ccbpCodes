#DifferenceBetweenMaxAndMin

given_list = input().split(",")
num_list = []
for char in given_list:
    char = int(char)
    num_list += [char]

sorted_num_list = sorted(num_list)
largest = max(sorted_num_list)
smallest = min(sorted_num_list)
difference = largest - smallest 
print(difference)