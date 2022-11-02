#IndivisibleNumbers

number_n = int(input())

is_k = 0
for i in range(1,number_n+1):
    k_numbers = 0 
    for j in range(2,11):
        condition = i % j == 0
        if condition == False:
            k_numbers = k_numbers +1
    if k_numbers == 9:
        is_k = is_k + 1
        
print(is_k)
        
        

