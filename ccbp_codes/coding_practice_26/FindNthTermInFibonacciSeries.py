#FindNthTermInFibonacciSeries

def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1)+fibonacci(n-2)


def get_fibonacci_series(n):
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
# call the fibonacci function
fib = fibonacci(n)
print(fib)
