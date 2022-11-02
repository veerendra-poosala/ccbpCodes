#OneColor

#Given a string of length N,made up of only uppercase character 'R' and 'G', 
#where "R" stands for Red and "G" stands for Green.
#Find out the minimum number of characters you need to change to make the whole string of the same color.

input_line = input()
input_line = input_line.upper()
length = len(input_line)
red = "R"
green = "G"
red_count = 0
green_count = 0

for char in input_line:
    if char == red:
        red_count = red_count + 1 
    elif char == green:
        green_count = green_count +1 
        
if red_count < green_count:
    result = length - green_count
    print(result)
else:
    result = length - red_count
    print(result)
