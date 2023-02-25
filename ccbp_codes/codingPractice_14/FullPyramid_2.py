#FullPyramid_2

rows_n = int(input())

for i in range(1,rows_n+1):
    result =""
    spaces = " "*(rows_n-i)
    
    for j in range(1,i +1):
        
        result=result+str(j)+" "
    print(spaces+result)
