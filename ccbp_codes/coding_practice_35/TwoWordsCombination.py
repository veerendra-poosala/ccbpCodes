#TwoWordsCombination

#accroding problem we need to get unique combinations so, we can use combinations formula to get the number of combinations.
#combinations: Out of 'n' different elements 'r' elements can be selected in two ways.
#without repition : nCr ways
#with repition : (n+r-1)Cr ways
#nCr = (n!) / (n-r)!

def find_factorial(num):
    if num <= 1:
        return num
    return num*find_factorial(num-1)

def get_total_combinations_count(given_input_str):
    
    input_list = given_input_str
    n = len(input_list)
    r = 2 #here we need olny two words combination
    #finding any repeated items in the list
    count = 1
    for i in range(len(input_list)):
        item = input_list[i]
        c = input_list.count(item)
        if c > count:
            count = c 
    
    #finding possible combinations count 
    num = n
    if count > 1:
        num = (n+r-1)
    numaretor_factor = find_factorial(num)
    denominator_1_factor = find_factorial((num-r))
    denominator_2_factor = find_factorial(r)
    denominator = denominator_1_factor * denominator_2_factor
    combinations = int(numaretor_factor / denominator)
    return combinations
 
def get_combinations(input_list,length=0,c_list = [], counter=0):
    comb_list = c_list
    sub_list = []
    length = length
    #print("length",length)
    
    #ordering list in a ascending order 
    ord_input_list = input_list.copy()
    #print("counter",counter)
    #print("ord_input_list",ord_input_list)
    
    for i in range(len(ord_input_list)):
        if i == (len(ord_input_list) - 1):
            break
        item_1 = ord_input_list[0]
        item_2 = ord_input_list[(i+1)]
        item = item_1 + " " + item_2
        if item in comb_list:
            break
        sub_list += [item]
         
    comb_list += sub_list
    #print("comb_list",comb_list)
    if counter == (length-1):
        return comb_list
        
    #removing first item for every iteration to get the new combination
    ord_input_list.pop(0)
    updated_list = ord_input_list
    #print("updated_list",updated_list)
    
    return get_combinations(updated_list,length, c_list=comb_list, counter = counter+1)

if __name__ == "__main__":
    given_input_str_list = input().split()
    given_input_str_list.sort()
    #print(given_input_str_list)
    length = len(given_input_str_list)
    
    combinations = get_combinations(given_input_str_list,length=length)

    #to remove the duplicates we are converting combinations list into set
    comb_set = set(tuple(combinations))
    comb_list = list(comb_set)
    comb_list.sort()
    
    #just to check the combinations count
    #comb_coount = get_total_combinations_count(given_input_str_list)
    #print(comb_coount)
    
    #print(comb_list)
    for item in comb_list:
        print(item)
    

