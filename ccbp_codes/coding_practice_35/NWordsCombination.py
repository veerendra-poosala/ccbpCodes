#NWordsCombination

def generate_3_combinations(words, n=0, comb_1_list=[], counter = 0):
    words = sorted(words) # Sort the inputs words
    items = list(range(len(words))) #will give the list of ranges i.e [0, 1, 2] where the length of the word is 3
    combinations_1 = comb_1_list  #create an empty list
    if counter == 0:
        for item in items:   #  iterate over the length of the input
            combinations_1.append([item]) # Generating one word combinations
        if n == 0:
            return words
         
    #Generating two words combinations by adding one more word to one-word combinations
    combinations_2 = []  #define an empty list
    #print("combinations_1",combinations_1)
    for combination in combinations_1: # iterating on one word combinations
        for item in items: # iterating on the sorted list
            #print("combination[-1]",combination[-1])
            if item > combination[-1]: # checking the word is next to the combination
                combinations_2.append(combination + [item]) # concatinating elements in one word combination and next elements
    #print("combinations_2",combinations_2)
    
    if n <= 1:
        #As we have stored indexes in combinations_3 now from below, we store words of that index in word_combinations
        word_combinations = []
        for combination in combinations_2:
            word_combination = []
            for index in combination:
                word_combination.append(words[index])
            word_combinations.append(tuple(word_combination))
        return sorted(set(word_combinations))
    return generate_3_combinations(words, n =n-1, comb_1_list = combinations_2, counter = counter+1 )

if __name__ == "__main__":
    #Read the input as a list, call the callback function and pass the input as an argument.
    words = input().split()
    n = int(input())
    all_combinations = generate_3_combinations(words,(n-1))
    #print(all_combinations)
    if n == 1:
        for combination in all_combinations:
            print(combination)
    else:
        for combination in all_combinations:  #for each combination in all_combinations
          print(' '.join(combination))     #print the combination
        
    
