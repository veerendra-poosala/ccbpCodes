#print function is used to print the output on display or screen
print("hello world")
#input function is used to get the data from user
#here name is the variable ,variable is a name location is used to store data
#name=input("Enter yout name : ")
#print(name)


#declaring multiple variables
a,b,c = "ram" , "sita" ,12
print( "a : " + a)
print("b : " +b)
#string and integer value concatination is not possible so ,we used explicit conversion method " str() " to convert int to string.
print("c : " + str(c))

name = "ram"
aliasName = "sri ramachandrudu"
print("name : " + name)
print("alilas : "+ aliasName)
#inter-changing variables 
name,aliasName = aliasName ,name
print("After inter-changing the name and surname values results will be below lines ")
print("name : " + name)
print("alias : "+ aliasName)


#number system
#In python operator precedence is PEMDAS { () => ** => * => / , // , % => + => - }

number1 =10000
print("number1 : " ,number1,sep="  ",end=" ") #using print default argumets to print  string and int without type casting in a single line
print() #To print the empty line
print("type of number1 is ",type(number1),sep=" ", end=" ")


