#FizzBuzz

def fizz_buzz(number):
    is_divisble_by_3 = number % 3 == 0
    is_divisble_by_5 = number % 5 == 0
    
    if is_divisble_by_3 and is_divisble_by_5:
        return "FizzBuzz"
    elif is_divisble_by_3:
        return "Fizz"
    elif is_divisble_by_5:
        return "Buzz"
    
    else:
        return number


number = int(input())
result = fizz_buzz(number)
print(result)