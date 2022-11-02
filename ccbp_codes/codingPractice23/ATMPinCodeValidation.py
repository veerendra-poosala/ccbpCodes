#ATMPinCodeValidation


def validate_atm_pin_code(pin):
    is_valid_pin_lenth = len(pin)==4 or len(pin) == 6
    is_valid_pin = False
   
    if is_valid_pin_lenth:
        if pin.isdigit() :
            is_valid_pin = True
        else:
            is_valid_pin = False
    else:
        is_valid_pin = False
        
    if is_valid_pin:
        return "Valid PIN Code"
    else:
        return "Invalid PIN Code"


pin = input()
result = validate_atm_pin_code(pin)
print(result)
