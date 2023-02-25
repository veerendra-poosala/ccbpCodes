#LeastCommonMultipleOfTheGivenTwoNumbers

m = int(input())
n = int(input())
lcm = 0
range_of_loop = m * n
for i in range(2,range_of_loop+1):
    condition_1 = i % m == 0
    condition_2 = i % n == 0
    if condition_2 & condition_1:
        lcm = i
        break 
print(lcm)