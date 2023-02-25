#ProductOfElementsInTheList

given_list = input().split()

product = 1 
int_list = []

for num in given_list:
    num = int(num)
    product *= num
    int_list += [num]
#print(int_list)
print(product)