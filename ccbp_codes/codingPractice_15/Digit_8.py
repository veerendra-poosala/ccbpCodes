#Digit_8

n = int(input())

rows = (2*n)+1
cols = n 

for i in range(1,rows+1):
    
    if i == 1:
        first_row = "* "*cols
        print(first_row)
    
    elif i == int((rows+1)/2):
        middle_row = "* "*cols
        print(middle_row)
    
    elif i == rows:
        middle_row = "* "*cols
        print(middle_row)
    
    elif i > 1 and i < int((rows+1) / 2):
        hollow_spaces = "  "*(cols-2)
        print("* "+ hollow_spaces+ "* ")
    
    elif i < rows and i > int((rows+1) / 2):
        hollow_spaces = "  "*(cols-2)
        print("* "+ hollow_spaces+ "* ")