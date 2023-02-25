def find_mean(num_list):
    length = len(num_list)
    sum = 0
    for num in num_list:
        sum += num 
    mean = sum / length 
    mean = round(mean,2)
    return "Mean: "+str(mean)

def find_median(num_list):
    new_list = sorted(num_list)
    length = len(new_list)
    is_odd = length % 2 == 1 
    if is_odd == True:
        index = int((length+1)/2)
        median = new_list[index - 1]
        return "Median: "+ str(median)
    else:
        index = int((length)/2)
        index_2 = index +1
        #print("1",new_list[index -1 ])
        #print("2",new_list[index_2 - 1])
        median = new_list[index - 1] + new_list[index_2 -1]
        median = round((median/2),2)
        
        
        return "Median: "+str(median)


def find_mode(num_list):
    new_list = sorted(num_list)
    length = len(new_list)
    
    max_rep = 0
    for num in new_list:
        count = 0
        for n in new_list:
            if num == n:
                count += 1
        if max_rep <= count:
            max_rep = count
    #print("max_rep",max_rep)
    #finding most repeated number 
    max_list = []
    
    for digit in new_list:
        count = 0
        for d in new_list:
            if digit == d:
                count += 1 
        if max_rep == count:
            max_list += [digit]
    #print("max_list", max_list)
    ref_digit = max_list[0]
    mode = [ref_digit]
    #print("mode",mode)
    #print("max_list",max_list)
    for i in range(1,len(max_list)):
        if max_list[i] != ref_digit:
            mode += [max_list[i]] 
            ref_digit = max_list[i]
            
    final_mode = ''
    for num in mode:
        num = str(num)
        final_mode += num + " "
       
    return "Mode: "+ final_mode
    #return mode
   


num_list = list(map(int, input().split()))
# Call the appropriate functions and print the results
mean = find_mean(num_list)
print(mean)
median = find_median(num_list)
print(median)
mode = find_mode(num_list)
print(mode)