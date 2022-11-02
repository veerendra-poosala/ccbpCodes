#HollowDiamond_2

n = int(input())

rows = 2*n 
cols = 2*n 

count = -1

for i in range(1,rows+1):
    
    if i == 1 or i == rows:
        print("* "*rows)
        count = count + 4
        
    elif i > 1 and i <= int(rows/2):
        stars = "* "*(n+1-i)
        hollow_spaces =" "*(count)
        stars_r = " *"*(n+1-i)
        print(stars + hollow_spaces+stars_r)
        count = count+4
        #print("count_1",count)
        
    elif i > int(rows/2) and i < rows:
        count = count-4
        stars = "* "*(i-n)
        hollow_spaces =" "*(count)
        #print("count",count)
        stars_r = " *"*(i-n)
        print(stars + hollow_spaces+stars_r)
        
        
        
    
    
        
        