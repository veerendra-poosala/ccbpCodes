#CumulativeSum

terms_n = int(input())

sum = 0
for i in range(terms_n):
    
    number = int(input())
    #print("number",number)
    
    sum += number
    print(sum)
    
    