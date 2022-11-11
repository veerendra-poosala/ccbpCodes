#SimpleCalculator_2

#Basic arithmetic operations +,-,*,/,and %

def perform_arithmetic_operation(new_list):
    digit_1 = int(new_list[0]) #num_1
    digit_2 = int(new_list[2]) #num_2
    operator = new_list[1]
    
    #print("digit_1",digit_1,type(digit_1))
    #print("digit_2",digit_2,type(digit_2))
    #print("operator",operator)
    
    if operator == '+':
        return digit_1 + digit_2 
    elif operator == '-':
       
        return digit_1 - digit_2 
    elif operator == '*':
        return digit_1 * digit_2
    elif operator == "/":
        return digit_1 / digit_2 
    elif operator == "%":
        return digit_1 % digit_2



given_input = input().split()
result = perform_arithmetic_operation(given_input)
print(result)
