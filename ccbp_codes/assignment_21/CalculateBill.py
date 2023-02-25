#CalculateBill

def calculate_bill(amount):
    if amount < 500:
        discount = (5/100)*amount
        total_bill = amount - discount
        return total_bill
    elif amount >= 500 and amount < 2500:
        discount = (10/100)*amount
        total_bill = amount - discount
        return total_bill
    elif amount >= 2500:
        discount = (20/100)*amount
        total_bill = amount - discount
        return total_bill
    
amount = int(input())
result = calculate_bill(amount)
print(result)
