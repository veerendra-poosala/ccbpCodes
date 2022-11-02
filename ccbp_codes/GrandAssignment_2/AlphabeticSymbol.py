#AlphabeticSymbol

rows_n = int(input())

alphabets ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = len(alphabets)
#print(length)

for i in range(1,rows_n+1):
    concate = ""

    if i == 1:
        print(alphabets[0]+" ")

    elif i == rows_n:
        for j in range(rows_n):
            char = alphabets[j]
            concate = concate +char+" "
        print(concate)
        
    elif i > 1 and i < rows_n:
        start = 0
        end = i
        for l in range(start,end):
            char = alphabets[l]
            concate = concate +char+" "
        print(concate)
            
        
            