#SumOfNonPrimes

rows_n = int(input())

sum = 0
ref = 1
for i in range(rows_n):
    factors = 0
    number = int(input())
    if ref < number:
        ref = number
    for j in range(1,ref+1):
        condition = number % j == 0
        if condition:
            factors = factors + 1 
    if factors > 2:
        sum = sum + number
print(sum)
        
            