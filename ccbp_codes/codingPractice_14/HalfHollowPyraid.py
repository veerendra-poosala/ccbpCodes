#HalfHollowPyraid

rows_n = int(input())
start = 1
end = 2
for i in range(1,rows_n+1):
    
    if i ==1:
        print("* "*i)
    elif i == rows_n:
        print(("* ")*i)
    else:
        hollow_spaces ="  "*(i-2) #doublespaces
        
        print("* "+hollow_spaces+"* ")
        
        
        
        
        