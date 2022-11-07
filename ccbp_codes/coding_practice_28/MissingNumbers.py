#MissingNumbers

def missing_numbers(given_list):
    
    #1)converting into int_list
    int_list = []
    for num in given_list:
        num = int(num)
        int_list += [num]
    
    #2)updating the int_list in ascending order
    int_list.sort()
    #print(int_list)
    
    #3)Finding the missing_numbers in series 1 to end_range.
    end_range = int_list[-1] 
    #print("end_range",end_range)
    new_int = []
    for i in range(1,end_range):
        condition = int_list[i-1] != i #checking missing number in int_list
        if condition == True  :
            int_list.insert((i-1),i) #updating int_list
            new_int += [i]
        
    return new_int
    
    


#Taking space-separated integers as input 

given_list = input().split()

result = missing_numbers(given_list)
print(result)