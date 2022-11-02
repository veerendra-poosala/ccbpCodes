'''Strings : strings in python are identified as a contiguous set of characters represented in the
quotation marks.

'''
'''
name = "laxman"
print(name)

#printing last character from name
print("Last character : "+name[-1])

#printing length of variable: name
print("Length of variable name is : "+str(len(name)))

#slicing
print(name[::]) #slicing : from start to stop and stepover is 1 by default

#you can print string multiple times
print(5*name,sep="  ")

#strings are immutable means you can not update by it's index position

#raw stirng

file_name = r"strings_python.py"

print(file_name)

#string methods

#1)upper : converts string into uppercase
upper_ = name.upper()
print("Upper casing  version of the 'name' variable : " + upper_)

#2)lower : converts string into lowercase
lower_case = name.lower()
print("Lower casing version of the 'name' variable : "+ lower_case)

'''

a = "ravi"
b =a[::-1]
print(b)