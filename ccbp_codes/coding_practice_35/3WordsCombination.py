#3WordsCombination

def generate_3_combinations(words):
    words = sorted(words) # Sort the inputs words
    items = list(range(len(words))) #will give the list of ranges i.e [0, 1, 2] where the length of the word is 3
    combinations_1 = []  #create an empty list
    for item in items:   #  iterate over the length of the input
        combinations_1.append([item]) # Generating one word combinations


    #Generating two words combinations by adding one more word to one-word combinations
    combinations_2 = []  #define an empty list
    print("combinations_1",combinations_1)
    for combination in combinations_1: # iterating on one word combinations
        for item in items: # iterating on the sorted list
            #print("combination[-1]",combination[-1])
            if item > combination[-1]: # checking the word is next to the combination
                combinations_2.append(combination + [item]) # concatinating elements in one word combination and next elements


    #Similar to three words combinations. We concatenate the next words into a two-words combination.
    combinations_3 = [] #define an empty list
    print("combinations_2",combinations_2)
    for combination in combinations_2:  
        for item in items:
            if item > combination[-1]: # checking if item is next word of last word in the two word combination
                combinations_3.append(combination + [item])

    print("combinations_3",combinations_3)
    #As we have stored indexes in combinations_3 now from below, we store words of that index in word_combinations
    word_combinations = []
    for combination in combinations_3:
        word_combination = []
        for index in combination:
            word_combination.append(words[index])
        word_combinations.append(tuple(word_combination))
    return sorted(set(word_combinations))


#Read the input as a list, call the callback function and pass the input as an argument.
words = input().split()
n = int(input())
all_combinations = generate_3_combinations(words)
for combination in all_combinations:            #for each combination in all_combinations
  print(' '.join(combination))             #print the combination
    
    
