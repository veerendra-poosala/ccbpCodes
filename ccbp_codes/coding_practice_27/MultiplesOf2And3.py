#MultiplesOf2And3

n = int(input())
even_list = []
odd_list = []

for i in range(1,n+1):
    even_num = i * 2 
    odd_num = i * 3 
    even_list += [even_num]
    odd_list += [odd_num]

#print(even_list)
#print(odd_list)

set_even = set(even_list)
set_odd = set(odd_list)

r1 = set_even - set_odd #difference
r1 = list(r1)
r1.sort()
print(r1)

r2 = set_even ^ set_odd  #symmetric difference
r2 = list(r2)
r2.sort()
print(r2)

