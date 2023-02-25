#FirstPrimeNumber

terms_n = int(input())


for i in range(terms_n):
    factors = 0
    number = int(input())
    for j in range(1,number+1):
        condition_1 = number % j == 0 # checking factors
        if condition_1:
            factors = factors + 1
    
    if factors == 2:
        print(number)
        break