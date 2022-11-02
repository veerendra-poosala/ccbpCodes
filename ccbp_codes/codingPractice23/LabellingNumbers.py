#LabellingNumbers

def show_numbers(number):
    for i in range(number+1):
        if i % 2 == 0:
            print(str(i)+" "+"EVEN")
        elif i % 2 == 1:
            print(str(i)+" "+"ODD")


number = int(input())
show_numbers(number)
