#code for printing pattern Inverted Half Pyramid

n = int(input())

for i in range(n):
    result = "" 
    for j in range(1,(n+1-i)):
        result = result +str(j)+" "
    print(result)