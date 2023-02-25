#PythagorasTriplets

limit = int(input())

#a,b,c = 0,0,0
sum = 0
#condition = a**2 + b**2 == c**2
#print(condition)
for a in range(2,limit+1):
    for b in range(2,limit +1):
        for c in range(2,limit+1):
            square_a = a**2
            square_b = b**2
            square_c = c**2
            condition = square_a + square_b == square_c
            if condition == True and a < b and c > b:
                sum = sum +1
print(sum)
                