#Acronyms 

#sample_input =  "Indian Administrative Service"

given_abbreviaton = input()

new_list = given_abbreviaton.split()
#print(new_list)
length = len(new_list)

result_list = []

for i in range(length):
    #print("i",new_list[i])
    for j in range(i+1):
        if j == 0:
            result_list += new_list[i][j]
            #print("j",new_list[i][j])

#print(result_list)
result_string = ".".join(result_list)
print(result_string)



