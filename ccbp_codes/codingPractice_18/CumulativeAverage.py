#CumulativeAverage

terms_n = int(input())

sum = 0 

for i in range(1,terms_n+1):
    number = int(input())
    sum += number
    average = sum / i
    print(round(average,3))