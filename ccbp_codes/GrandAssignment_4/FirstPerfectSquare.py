#FirstPerfectSquare

m = int(input())
n = int(input())
msg = ""
for i in range(m,n+1):
    float_m = float(i)
    root_m = round(i ** 0.5,1)
    square = root_m * root_m
    #print("float_m",float_m,"root_m",root_m,"square",square)
    perfect_square = float_m == square
    if perfect_square == True:
        msg = str(i)
        break
    else:
        msg = "No Perfect Square"
print(msg)