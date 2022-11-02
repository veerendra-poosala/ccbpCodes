#Diamond

n = int(input())

rows = (2*n)-1
count = 1

for i in range(1,rows+1):
    
    if i == 1 or i == rows:
        dots_set = ". "*(n-1)
        zeros_set = "0 "*(1)
        print(dots_set+zeros_set+dots_set)
        count = count + 2
    
    elif i > 1 and i <= int((rows+1)/2): 
        dots_set = ". "*(n-i)
        zeros_set = "0 "*(count)
        print(dots_set+zeros_set+dots_set)
        count = count + 2
        count_lower = count - 4
        #print(count_lower)
    elif i > int((rows+1)/2) and i < rows:
        dots_set = ". "*(i-n)
        zeros_set = "0 "*(count_lower)
        print(dots_set+zeros_set+dots_set)
        count_lower = count_lower - 2
        
        