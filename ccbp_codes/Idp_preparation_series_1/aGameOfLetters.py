#aGameOfLetters
def perform_rotation(word,index):
    part_1 = word[:index]
    part_2 = word[index:]
    new_word = part_2 + part_1
    #print(new_word)
    return new_word


def arrange_list_items_starts_with_vowel(given_sentence):
    vowels_list = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    result_list = ''
    for i in range(len(given_sentence)):
        word = given_sentence[i]
        index = -1
        count = 0
        new_word = word
        for j in range(len(word)):
            if word[j] in vowels_list:
                index = word.index(word[j])
                break
            else:
                count += 1
        if count != len(word):
            new_word = perform_rotation(word,index)
        result_list += new_word + ' '
    return result_list

def main():
    given_sentence = input().split()
    result = arrange_list_items_starts_with_vowel(given_sentence)
    print(result)
main()