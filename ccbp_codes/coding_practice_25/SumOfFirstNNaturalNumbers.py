#SumOfFirstNNaturalNumbers

def sum_of_numbers(n):
    if n <= 0:  # Base case
        return 0
    else:
        return n + sum_of_numbers(n-1)  # Recursion


num = int(input())
result = sum_of_numbers(num)
print(result)
