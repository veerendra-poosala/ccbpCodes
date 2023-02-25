#NTermsInFibonacciSeries

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

def get_fibonacci_series(n):
    if n > 0:
        num_list = [0]
        a = 0 
        b = 1
        for i in range(n-1):
            c = a + b 
            b = a
            a = c
            num_list += [c]
        return num_list


n = int(input())
# Call the get_fibonacci_series function
r1 = get_fibonacci_series(n)
print(r1)