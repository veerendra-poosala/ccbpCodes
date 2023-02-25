#AccessingNestedLists

list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]

n = int(input())

new_list = []
result_list = []
#getting inputs from user
for i in range(n):
    given_inputs = list(map(int,input().split())) 
    new_list += [given_inputs]

#AccessingNestedLists
for i in range(len(new_list)):
    d_1 = new_list[i][0]
    d_2 = new_list[i][1]
    result_list += [list_a[d_1][d_2]]
        
print(result_list)