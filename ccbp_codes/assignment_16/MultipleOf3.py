#MultipleOf3 

terms_n = int(input())

for i in range(terms_n):
    b = int(input())
    is_mul_of_3 = b % 3 == 0
    if is_mul_of_3:
        print(b)