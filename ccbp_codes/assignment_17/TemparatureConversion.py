
#TemparatureConversion

#c = (f - 32)*5 / 9 #Formula to convert Fahrenheit to Celsius
#c = (k - 273) #Formula to convert  Kelvin to Celsius

given_temp = input()
length = len(given_temp)

for char in given_temp:
    temparature = given_temp[:(length-1)]
    temparature = round(float(temparature),2)
    
    if char == "C":
        celsius_to_farenheit = (9/5)*temparature + 32 #converting Celsius to Fahrenheit
        celsius_to_kelvin = temparature + 273  #converting celsius to kelvin
        celsius_to_kelvin = round(celsius_to_kelvin,2)
        
        print(str(temparature) + "C")
        print(str(celsius_to_farenheit) + "F")
        print(str(celsius_to_kelvin) + "K") 
    
    elif char == "F":
        
        
        fahrenheit_to_celsius = (temparature - 32)*5 /9
        fahrenheit_to_celsius = round(fahrenheit_to_celsius,2)
        
        fahrenheit_to_kelvin = fahrenheit_to_celsius + 273
        fahrenheit_to_kelvin = round(fahrenheit_to_kelvin,2)
        
        print(str(fahrenheit_to_celsius)+"C")
        print(str(temparature) + "F")
        print(str(fahrenheit_to_kelvin) + "K")
    
    elif char == "K":
        
        temparature_in_kelvin = temparature
        kelvin_to_celsius = temparature_in_kelvin - 273
        
        celsius_to_farenheit = (9/5)*kelvin_to_celsius + 32 
        celsius_to_farenheit = round(celsius_to_farenheit,2)
        
        print(str(kelvin_to_celsius) + "C")
        print(str(celsius_to_farenheit)+"F")
        print(str(temparature_in_kelvin)+"K")
        
        
        
        
        

 