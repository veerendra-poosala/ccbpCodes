#MultipleOf5

terms_n = int(input())

for i in range(terms_n):
    b = int(input())
    is_mlutiple_of_5 = b % 5 == 0
    if is_mlutiple_of_5:
        break 
    print(b)
    