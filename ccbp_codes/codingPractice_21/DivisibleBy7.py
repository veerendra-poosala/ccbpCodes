#DivisibleBy7

def divisible_by_seven(arg_1):
    is_divisible_by_7 = arg_1 % 7 == 0
    print(is_divisible_by_7)


n = int(input())
divisible_by_seven(n)
