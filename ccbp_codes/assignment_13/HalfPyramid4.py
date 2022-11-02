#HalfPyramid4

#Initializing variables
start_range_n = int(input())
terms_k = int(input())
end_range =start_range_n + 1

#for loop to get end value of the Halfpyramid
for i in range(1,terms_k+1):
    result =""
    
    for j in range(start_range_n,end_range):
        result = str(j)+" "+result
        start_range_n = j +1
        end_range = j + i +2
    #print(result)

rev_start_range = j 
#print(rev_start_range)
rev_end_range = rev_start_range +1

#for loop for Halfpyramid range starts from j
for n in range(1,terms_k+1):
    string_out =""
    for m in range(rev_start_range,rev_end_range):
        string_out = str(m)+" "+string_out
    
    end_value = rev_start_range
    #print("end_value",end_value)
    rev_start_range = end_value - n -1
    #print("rev_start_range",rev_start_range)
    rev_end_range =  rev_start_range +n+1
    #print("rev_end_range",rev_end_range)
    #print(n)
  
    print(string_out)
        
        
        
        