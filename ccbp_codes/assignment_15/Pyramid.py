#Pyramid

rows_n = int(input())
count = 1
for i in range(1,rows_n+1):
    dots_pattern = ". "*(rows_n - i)
    if i == 1:
        zero_pattern ="0 "*count
        print(dots_pattern+zero_pattern+dots_pattern)
    elif i == rows_n:
        zero_pattern ="0 "*count
        print(dots_pattern+zero_pattern+dots_pattern)
    
    else:
        zero_pattern ="0 "*count
        print(dots_pattern+zero_pattern+dots_pattern)
    
    count = count+2
        
    