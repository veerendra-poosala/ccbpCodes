#APowerB
def calculate_power(x, y):
    base_value = x 
    power_value = y
    if y == 0:
        return 1
    else:
        x = base_value
        y = power_value - 1
        return base_value * calculate_power(x,y) 


a = int(input())
b = int(input())
# Call the calculate_power function
result = calculate_power(x=a,y=b)
print(result)