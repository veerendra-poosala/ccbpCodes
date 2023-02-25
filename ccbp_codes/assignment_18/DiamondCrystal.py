#DiamondCrystal

n = int(input())
rows = 2*n 
cols = 2*n 

count = 0

for i in range(1,rows+1):
    
    if i == 1 :
        left_spaces = " "*(n-1)
        backward_slash = "\\"
        hollow_spaces = " "
        print(left_spaces+"/"+backward_slash)
        count += 2
        
    elif i > 1 and i <= int((rows+1)/2):
        left_spaces = " "*(n-i)
        backward_slash = "\\"
        hollow_spaces = " "*count
        print(left_spaces+"/"+hollow_spaces+backward_slash)
        count += 2
        #print(count)
        count_lower = count - 2
        
    elif i > int((rows+1) / 2) and i <= rows:
        left_spaces = " "*(i-n-1)
        hollow_spaces = " "*count_lower
        print(left_spaces+"\\"+hollow_spaces+"/")
        count_lower -= 2
        
        
        