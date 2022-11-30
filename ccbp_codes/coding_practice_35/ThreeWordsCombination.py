#ThreeWordsCombination

#Problem Staement: Given a sentence as input, print all the unique combinations of 
#thre words lexicographical order.
#Input format : The Input will be a single line containing a sentence.
#Output format :The Output should be multiple lines, each line containing the unique combinations
#of three words in lexicographical order.


def get_2_word_combinations_for_each_item(input_list):
    sub_list = []
    ord_input_list = input_list.copy()
    for i in range(len(ord_input_list)):
        if i == (len(ord_input_list) - 1):
            break
        item_1 = ord_input_list[0]
        item_2 = ord_input_list[(i+1)]
        item = item_1 + " " + item_2
        sub_list += [item]
    return sub_list
    

def get_3_word_unique_comb_list(given_list , length=0, comb_3_list=[], counter=0 ):
    updated_list = given_list.copy()
    combinations_list = comb_3_list
    l = length
    #print("updated_list",updated_list,"l",l)
    
    #getting individual item combinations except last item
    list_for_2_word_comb =updated_list[:-1]
    #print("list_for_2_word_comb",list_for_2_word_comb)
    length_2_word_comb = len(list_for_2_word_comb)
    comb_2_new_list = get_2_word_combinations_for_each_item(list_for_2_word_comb)
    #print("comb_2_list",comb_2_new_list)
    
    each_combination = []
    satrt = 2
    for j in range(len(comb_2_new_list)):
        for i in range(satrt,len(updated_list)):
            item_1 = comb_2_new_list[j]
            item_2 = updated_list[i]
            item = item_1+" "+item_2
            if item in combinations_list:
                break
            each_combination += [item]
            #print("each_combination",each_combination)
        satrt += 1
    
    combinations_list += each_combination
    #print("combinations_list",combinations_list)
    #print("counter",counter)
    
    ##loop termination condition
    if len(updated_list) <= 3 :
        if len(updated_list) < 3:
            new_string = " ".join(updated_list)
            list_end = [new_string]
            return list_end
        resultant_list = combinations_list
        return resultant_list
    
    #removing element from updated_list to update the original list
    updated_list.pop(0)
    #print("updated_list",updated_list)
    
    return get_3_word_unique_comb_list(updated_list, length=l, comb_3_list=combinations_list,counter=counter+1)

if __name__ == "__main__":
    input_list = input().split()
    input_list.sort()
    length = len(input_list)
    #print("input_list",input_list)
    
    #getting two word combinations upto last word, last word not included
    #input_1_list = input_list[:-1]
    #comb_2_individual = get_2_word_combinations_for_each_item(input_1_list)
    #print("comb_2_individual",comb_2_individual)
    combinations = get_3_word_unique_comb_list(input_list,length=length)
    
    #to remove the duplicates we are converting combinations list into set
    comb_set = set(tuple(combinations))
    comb_list = list(comb_set)
    comb_list.sort()
    
    for item in comb_list:
        count = comb_list.count(item)
        print(item)