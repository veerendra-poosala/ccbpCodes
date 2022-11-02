#ReverseOrder

terms = int(input())

new_list = []
for i in range(terms):
    n = input()
    new_list = [n]+new_list
    
#print(new_list)
for char in new_list:
    print(char)
