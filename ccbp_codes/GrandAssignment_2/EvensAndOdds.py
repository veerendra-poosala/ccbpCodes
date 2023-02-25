#EvensAndOdds

start_range_m = int(input())
end_range_n = int(input())

even_count = 0 
odd_count = 0

for i in range(start_range_m,end_range_n+1):
    is_even = i % 2 == 0 
    is_odd = i % 2 == 1 
    if is_even:
        even_count = even_count +1 
    elif is_odd:
        odd_count = odd_count + 1 
        
print(odd_count)
print(even_count)