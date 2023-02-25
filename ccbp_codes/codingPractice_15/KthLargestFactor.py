#KthLargestFactor

n = int(input())
k_th_largest_factor = int(input())

factor = n 
k_th_largest_factor_is_found = False
count = 0
for i in range(1,n+1):
    if not(k_th_largest_factor_is_found):
        if (n % factor) == 0:
            count = count+1
        if k_th_largest_factor == count:
            print(factor)
            k_th_largest_factor_is_found = True
      
    factor = factor -1
