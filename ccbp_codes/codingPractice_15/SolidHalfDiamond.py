#SolidHalfDiamond 

rows_n = int(input())
terms = (2 * rows_n) - 1 

for i in range(1,terms+1):
    
    if i == 1 :
        print("* ")
    elif i == int((terms+1) / 2):
        print(("* ")*rows_n)
    elif i == terms:
        print("* ")
    else:
        if i > 1 and i < int((terms+1)/2):
            print(("* ")*i)
        if i > int((terms+1) / 2) and i < terms:
            print(("* ")* (terms+1-i))