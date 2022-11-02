#HollowDiamond

cols_n = int(input())
rows = (2*cols_n)-1

count = 1
start_range = 64 # initiating unicode value reference
for i in range(1,rows+1):
    
    if i == 1 or i == rows:
        left_spaces = " "*(cols_n-1)
        character = "A"*(1)
        print(left_spaces+character)
        
    elif i > 1 and i <= int((rows+1) /2):
        char_unicode = start_range + i
        char = chr(char_unicode)
        left_spaces = " "*(cols_n-i)
        hollow_spaces = " "*(count)
        print(left_spaces+char+hollow_spaces+char)
        count = count+2
        count_lower_section = count - 4
        
    elif i > int((rows+1) /2) and i < rows:
        char_unicode_lower = char_unicode - (i - cols_n) 
        char = chr(char_unicode_lower)
        left_spaces = " "*(i-cols_n)
        hollow_spaces = " "*count_lower_section
        print(left_spaces+char+hollow_spaces+char)
        count_lower_section = count_lower_section - 2
        