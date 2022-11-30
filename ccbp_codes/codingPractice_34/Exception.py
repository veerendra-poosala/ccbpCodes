#Exception

def perform_div_operation():
    a,b = input().split()
    
    try:
        a = int(a)
        b = int(b)
        c = a / b 
        return c
    
    except ZeroDivisionError:
        return "Denominator can't be 0"
    except ValueError:
        return "Input should be an integer"
    except:
        return "Division not possible"
        



res = perform_div_operation()
print(res)