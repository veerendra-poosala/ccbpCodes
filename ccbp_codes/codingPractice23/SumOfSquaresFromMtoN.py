#SumOfSquaresFromMtoN

def sum_of_squares_m_to_n(m, n):
    sum = 0
    for num in range(m,n+1):
        num = num **2
        sum += num
    return sum


m = int(input())
n = int(input())

result = sum_of_squares_m_to_n(m,n)
print(result)
