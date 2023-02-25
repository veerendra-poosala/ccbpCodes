#AllPossibleSubsets

def get_n_word_combinations(words, n=0, comb_list =[], counter=0):
    new_ord_words = sorted(words)
    length_of_words = len(new_ord_words)
    indexes_list = list(range(length_of_words))
    
    comb1_list = comb_list
    if counter == 0:
        for i in indexes_list:
            comb1_list.append([i])
        if n <= 0:
            return new_ord_words
    #print("comb1_list",comb1_list)
    comb2_list = []
    for comb in comb1_list:
        for i in indexes_list:
            if i > comb[-1]:
                comb2_list.append(comb + [i])
    #print("comb2_list",comb2_list)
    
    if n <= 1:
        words_list = []
        for comb in comb2_list:
            words_item = []
            for c  in comb:
                if new_ord_words[c] not in words_item:
                    words_item.append(new_ord_words[c])
            words_list.append(tuple(words_item))
            #removing duplicates
            new_words_list = sorted(set(words_list))
        return new_words_list
    return get_n_word_combinations(new_ord_words,n = n-1, comb_list=comb2_list, counter=counter+1)
    

words_list = input().split()
#print("words", words)

words_list = set(tuple(words_list))
words = list(words_list)
words.sort()
length = len(words)

res_list = []
for n in range(length):
    combinations = get_n_word_combinations(words,n=n)
    if n == 0:
        res_list.extend(combinations)
        #for item in combinations:
            #combinations_list_2.extend([item])
    else:
        for each_comb in combinations:
            #count = combinations.count(each_comb)
            #print("count",count)
            #print("length",len(each_comb))
            #each_comb = list(each_comb)
            result = " ".join(each_comb)
            res_list.extend([result])
    


unique_combination=[]  #create a variable to store unique combinations 
for j in res_list: #iterate the combinations
    if j not in unique_combination: #use membership check method (in operator) to avoid duplicates 
        unique_combination.append(j) 
for item in unique_combination:
    count = unique_combination.count(item)
    #print("count",count)
    print(item)
    
    