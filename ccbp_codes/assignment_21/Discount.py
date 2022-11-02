#Discount

def get_discount(amount):
    if amount < 500:
        return "5%"
    elif amount >= 500 and amount < 2500:
        return "10%"
    elif amount >= 2500:
        return "20%"


amount = int(input())
result = get_discount(amount)
print(result)

