#ReverseTheLettersInWordsOfTheSentence

given_string = input()

list_1 = given_string.split()
#print(list_1)

reverse_list = []

for i in list_1:
    reverse_word = ""
    #print(i)
    for j in range(len(i)):
        reverse_word = i[j] + reverse_word
        #print(reverse_word)
    reverse_list += [reverse_word]

#print(reverse_list)

result_string = " ".join(reverse_list)
print(result_string)