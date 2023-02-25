#PrintingMessage

def message(arg_1, arg_2):
    msg = arg_1 + " is "+str(arg_2)+" years old."
    return msg

name = input()
age = int(input())
reuslt = message(name,age)
print(reuslt)
