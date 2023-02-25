#PrefixSuffix

#condition = first_word_suffix == prefix_of_next_word

def is_prefix_for_next_word(first_word,next_word):
    
    start_char = next_word[0]
    start_char_count = first_word.count(start_char)
     
    if start_char_count > 0:
        start_char_index = first_word.index(start_char)
        #print(start_char_index)
        suffix = ''
        prefix = ''
        count = 0
        
        #getting suffix word from first_word
        for i in range(len(first_word)):
            if i >= start_char_index:
                suffix += first_word[i]
                count += 1
        #print(suffix)
        
        #getting prefix word from next_word
        length_of_prefix_word = len(suffix)
        if len(suffix) > 0:
            for j in range(length_of_prefix_word):
                prefix += next_word[j]
            
        #print(prefix)
        if suffix == prefix:
            return suffix
        elif suffix != prefix or len(suffix) == 0:
            return "No overlapping"
    else:
        return "No overlapping"
    
first_word = input()
next_word = input()

result = is_prefix_for_next_word(first_word,next_word)
print(result)