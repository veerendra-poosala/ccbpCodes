#CompositeNumbersInTheRange

start_range_m = int(input())
end_range_n = int(input())

for i in range(start_range_m,end_range_n+1):
    factors = 0
    for j in range(1,end_range_n+1):
        
        condition_1 = i % j == 0
        if condition_1:
            factors = factors +1
    if factors > 2:
        print(i)