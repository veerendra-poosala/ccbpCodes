#InvertedFullPyramid_2

rows_n = int(input())

start_range = 1 

for i in range(1,(rows_n+1)):
    
    end_range = rows_n + 2 - i
    spaces =" "*(i -1)
    result =""
    for j in range(start_range,end_range):
        result = result+str(j)+" "
    print(spaces+result)
        