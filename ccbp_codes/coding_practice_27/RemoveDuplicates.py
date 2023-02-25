#RemoveDuplicates

num_list = list(map(int,input().split())) #input from user
num_list = set(num_list) #converting into set to remove the duplicates
num_list = list(num_list) #again converting back into lists
num_list.sort() #arranging into an ascending order
print(num_list)