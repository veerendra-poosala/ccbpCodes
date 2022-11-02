#HalfPyramid3

start_range_n = int(input())
terms_k = int(input())

i =1 
end_range = start_range_n 

for i in range(1,terms_k+1):
    result = ""
    for j in range(start_range_n,end_range+1):
        result = result +str(j)+" "
        start_range_n = j + 1 
        end_range = j + i + 1
    print(result)
