#WPatternWithAsterisk

rows_n = int(input())
count = 1
for i in range(1,rows_n+1):
    if i == 1:
        print("* "*((2*rows_n)-1))

    elif i == rows_n:
        left_spaces =" "*(i-1)
        hollow_spaces = " "*(count-3)
        print(left_spaces+"* "+hollow_spaces+"* ")
        
    elif i >1 and i < rows_n:
        left_spaces =" "*(i-1)
        hollow_spaces = " "*(count-3)
        stars = "* "*(rows_n+1 - i)
        print(left_spaces+stars+hollow_spaces+stars)
        
    
    count = count +2