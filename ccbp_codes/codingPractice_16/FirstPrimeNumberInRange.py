#FirstPrimeNumberInRange

start_range_m = int(input())
end_range_n = int(input())
is_prime = False

if start_range_m < 0 and end_range_n > 0:
    start_range_m = 2

for i in range(start_range_m, end_range_n):
    counter = 0
    for j in range(1,end_range_n+1):
        condition = i % j == 0 
        
        if condition :
            counter = counter+1
        
    if counter == 2  :
            is_prime = True
            print(i)
            break 
if counter > 2:

    print("No prime numbers in the given range")
            
            
    
    

    

    