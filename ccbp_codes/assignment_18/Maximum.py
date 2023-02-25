#Maximum

terms_n = int(input())

ref_input = int(input())
print(ref_input)

for i in range(terms_n-1):
    
    number = int(input())
    #print("number",number)
    if ref_input < number:
        ref_input = number
        print(ref_input)
    else:
        ref_input = ref_input
        print(ref_input)