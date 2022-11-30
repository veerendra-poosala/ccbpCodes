#Polynomial

n=int(input())

#taking all the inputs into a dict based on power values
polynomial_dict = {}

if n<=100:
    for i in range(n):
        power,coeff = map(int,input().split())
        if power not in polynomial_dict:
            polynomial_dict[power] = coeff
        elif power in polynomial_dict:
            old_value = polynomial_dict[power]
            polynomial_dict[power] = old_value + coeff

#converting dict to list to print           
polynomial_list =[]
for key,val in polynomial_dict.items():
    polynomial_list.append((key,val))
#print(polynomial_list)

#sorting list to print from max power to min power
polynomial_list = sorted(polynomial_list,reverse=True)

result = ""
for i in range(len(polynomial_list)):
    p = polynomial_list[i][0] #power
    c = polynomial_list[i][1] #coefficient
    next_c = 0
    msg =""
    
    #when max power we don't need to print operand sign before coefficient
    if i == 0:
        
        if c > 0:
            if c == 1:
                msg = "x^{}".format(str(p))
            else:
                msg = "{}x^{}".format(str(c),str(p))
        elif c < 0:
            if c == -1:
                msg = "-x^{}".format(str(p))
            else:
                c = c * -1
                msg = "-{}x^{}".format(str(c),str(p))
    elif i > 0 and i < len(polynomial_list)-2 :
        if c > 0:
            if c == 1:
                msg = " + x^{}".format(str(p))
            else:    
                msg = " + {}x^{}".format(str(c),str(p))
        elif c < 0:
            if c == -1:
                msg = " - x^{}".format(str(p))
            else:
                c = c * -1
                msg = " - {}x^{}".format(str(c),str(p))
    elif i == len(polynomial_list)-2:
        if c > 0:
            if c == 1:
                msg = " + x"
            else:    
                msg = " + {}x".format(str(c))
        elif c < 0:
            if c == -1:
                msg = " - x"
            else:
                c = c * -1
                msg = " - {}x".format(str(c))
    
    else:
        if c > 0:
            msg = " + {}".format(str(c),str(p))
        elif c < 0:
            c = c * -1
            msg = " - {}".format(str(c),str(p))
    
    result += msg
    
print(result)

        
