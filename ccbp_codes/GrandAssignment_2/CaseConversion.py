#CaseConversion

#convert CamelCasing to snake_casing

camelCasingLine = input()

result = ""

for i in range(1,len(camelCasingLine)):
    condition = camelCasingLine[i] == camelCasingLine[i].upper()
    if condition == False:
        result = result+camelCasingLine[i]
        #print(result)
    else:
        result = result + "_"+camelCasingLine[i]
        #print(result)
 
camelCasingLine = camelCasingLine[0]+result 
snake_casing_line = camelCasingLine.lower()
print(snake_casing_line)


        