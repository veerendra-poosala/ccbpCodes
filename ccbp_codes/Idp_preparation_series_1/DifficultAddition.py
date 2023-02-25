#DifficultAddition

def find_carry_numbers(num1,num2,smallest_number):
    sum_of_digits = 0
    count = 0
    for i in range(1,smallest_number+1):
        val_1 = int(num1[-i])
        val_2 = int(num2[-i])
        sum_of_digits = val_1 + val_2
        if sum_of_digits > 9:
            count += 1 
    return count

def difficult_addition(carry_numbers):
    msg = "Easy"
    if carry_numbers >= 1:
        msg = "Hard"
    return msg

def main():
    num_list =input().split()
    num1 = num_list[0]
    num2 = num_list[1]
    len_1 = len(num1)
    len_2 = len(num2)
    smallest_number = min(len_1,len_2)
    carry_numbers = find_carry_numbers(num1,num2,smallest_number)
    #print(carry_numbers)
    validate_carry_numbers=difficult_addition(carry_numbers)
    print(validate_carry_numbers)
main()