#RightTriangle

rows_n = int(input())

numbers ="1234567890"
count = 1
for i in range(1,rows_n+1):
    if i == 1:
        print(numbers[0]) 
    elif i == rows_n:
        result_1 = ""
        result_2 = ""
        
        for l in range(count):
            if l > int(count / 2):
                z = count - l
                result_2 = result_2 +str(z)
                
                #print(z)
                #print(l)
                #print(int(count))
            else:
                
                result_1 = result_1 + numbers[l]
                 
        print(result_1 + result_2)
         
    else:
        result_1 = ""
        result_2 = ""
        
        for l in range(count):
            if l > int(count / 2):
                z = count - l
                result_2 = result_2 +str(z)
                
                #print(z)
                #print(l)
                #print(int(count))
            else:
                
                result_1 = result_1 + numbers[l]
                 
        print(result_1 + result_2)
        
    count = count + 2
