#InvertedFullPyramid

rows_n = int(input())

start_range = 1 


for i in range(1,rows_n+1):
    result = ""
    end_range = (rows_n+2)-i
    spaces = " "*(i-1)
    for j in range(start_range,end_range):
        
        stars = "* "*j 
    result = stars+" "+result
    print(spaces+result)