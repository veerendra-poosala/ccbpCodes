#Digit_9 

n = int(input())
rows_n = (2*n)-1

for i in range(1,rows_n+1):
    if i == 1:
        print("* "*n)
    elif i == int((rows_n+1) / 2):
        print("* "*n)
    elif i == rows_n :
        print("* "*n)
    elif i > 1 and i < int((rows_n+1) / 2):
        hollow_spaces = "  "*(n-2)
        print("* "+hollow_spaces+"* ")
    elif i > int((rows_n+1) / 2) and i < rows_n:
        hollow_spaces = "  "*(n-1)
        print(hollow_spaces+"* ")
        
    
    