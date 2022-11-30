#MaxAndMinValueInListOfTuples

rows_n = int(input())
num_list = []

for i in range(rows_n):
    #taking space separated integers from user as a list items
    given_list = list(map(int,input().split()))
    #print(given_list)
    num_list += [given_list]
#print(num_list)

#creating new lists to separate min,max values based on positions
zero_index_list = []
one_index_list = []

for i in range(len(num_list)):
    length = len(num_list[i])
    for j in range(length):
        if j == 0:
            zero_index_list += [num_list[i][j]]
        elif j == 1:
            one_index_list += [num_list[i][j]]
#print(zero_index_list,one_index_list)

#Finding maximum and minimum for one_index_list and zero_index_list
maximum_at_zero_index_list = max(zero_index_list)
#print(maximum_at_zero_index_list)
minimum_at_zero_index_list = min(zero_index_list)
#print(minimum_at_zero_index_list)
minimum_at_one_index_list = min(one_index_list)
maximum_at_one_index_list = max(one_index_list)

#adding max and min values to a tuple and printing it
tuple_1 = (maximum_at_zero_index_list,minimum_at_zero_index_list)
tuple_2 = (maximum_at_one_index_list,minimum_at_one_index_list)

print(tuple_1,tuple_2 ,sep = "\n")

            
            
    

