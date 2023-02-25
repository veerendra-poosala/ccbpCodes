#CreateAndPrintList_2 

terms = int(input())

new_list = []
for i in range(terms):
    n = input()
    new_list += [n]
    
print(new_list)