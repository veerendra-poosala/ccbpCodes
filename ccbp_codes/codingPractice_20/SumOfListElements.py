#SumOfListElements

given_string = input()

num_list = given_string.split()
sum = 0
#new_list = []
#print(num_list)
for i in num_list:
    i = int(i)
    sum += i
    #new_list += [i]
#print(new_list)
print(sum)