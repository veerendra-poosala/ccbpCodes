#ReplaceAValue

def replace_old_value_with_new_value(matrix, old_value, new_value):
    num_list = matrix
    
    for i in range(len(num_list)):
        for j in range(len(num_list[i])):
            if old_value == num_list[i][j]:
                num_list[i][j] = new_value #using list mutability
                
    return num_list
        


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

values = input().split()
old_value, new_value = convert_string_to_int(values)

result = replace_old_value_with_new_value(num_list,old_value,new_value)
for res in result:
    print(res)
