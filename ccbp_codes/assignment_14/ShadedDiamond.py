#ShadedDiamond

rows_n = int(input())

terms = (2 * rows_n)-1

for i in range(1,terms+1):
    
    if i == 1:
        left_spaces_upper = " "*(rows_n - i)
        first_row  = "* "
        print(left_spaces_upper+first_row)

    elif i == int((terms+1)/2):
        left_spaces_upper = " "*(rows_n-i)
        exact_middle_row ="* "*rows_n
        print(left_spaces_upper+exact_middle_row)

    elif i == terms:
        left_spaces_lower = " "*(rows_n-1)
        last_row = "* "
        print(left_spaces_lower + last_row)
        
    else:
        if i > 1 and i < int((terms+1) /2):
            left_spaces_upper = " "*(rows_n-i)
            for s in range(1,(i+1)):
                solid_middle_row ="* "*s 
            print(left_spaces_upper+solid_middle_row)  
            
        elif i > int((terms+1) / 2) and i < terms:
            left_spaces_lower = " "*(i - rows_n)
            hollow_spaces = "  "*(terms - i-1) # hollow spaces = double spaces
            hollow_middle_rows = "* "+hollow_spaces+"* "
            print(left_spaces_lower+hollow_middle_rows)
    