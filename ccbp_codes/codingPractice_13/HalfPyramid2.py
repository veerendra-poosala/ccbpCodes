#HalfPyramid2

n = int(input())
i = 1 #initializing i = 0 because i value changing in for loop according to range.
start_range = 1 
end_range = i +1

for i in range(1,n+1):
    
    result = ""
    for j in range(start_range,end_range):
        result = result +str(j)+" "
        start_range = j+1 #updating start range value
        end_range = j+i+2
    print(result)