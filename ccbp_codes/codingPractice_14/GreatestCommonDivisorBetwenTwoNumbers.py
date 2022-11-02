#GreatestCommonDivisorBetwenTwoNumbers

m = int(input())
n = int(input())

count = 0

for i in range(2,n+1):
    condition_1 = m % i == 0
    condition_2 = n % i == 0
    
    if condition_1 and condition_2:
        is_greater = i
        count = count +1
        

if count == 0:
    print("1")
else:
    print(is_greater)