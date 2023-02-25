#Hallow Inverted Half pyramid_1

rows_n = int(input())

for i in range(1,rows_n+1):
    
    if i == 1:
        print("* "*rows_n) #first line
    elif i == rows_n:
        
        print("* ") #last line
    else:
        hollow_spaces = "  "*((rows_n-i-1)) #double spaces
        print("* "+hollow_spaces+"* ") #middle lines