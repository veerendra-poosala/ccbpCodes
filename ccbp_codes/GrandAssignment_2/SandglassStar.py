#SandglassStar

rows_n = int(input())
terms = (2*rows_n)-1

for i in range(1,terms+1):
    left_spaces = " "
    
    if i == 1 or i == terms:
        first_line = "* "*rows_n
        print(first_line)
        
    elif i == int((terms+1) / 2):
        left_spaces = " "*(rows_n-1)
        print(left_spaces+"* ")
        
    elif i > 1 and i < int((terms + 1)/2):
        left_spaces = " "*(i-1)
        stars ="* "*(rows_n+1-i)
        print(left_spaces+stars)
        
    elif i > int((terms+1)/2) and i < terms:
        left_spaces = " "*(terms - i)
        stars = "* "*((i+1)-rows_n)
        print(left_spaces+stars)
    
        