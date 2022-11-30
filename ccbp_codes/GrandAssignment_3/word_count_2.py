#word_count_2


def print_dict(word_count_dict):
    new_list = list(word_count_dict.items())
    new_list.sort()
    for i in range(len(new_list)):
        word = new_list[i][0]
        count = new_list[i][1]
        msg = "{0}: {1}".format(word,count)
        print(msg)

def count_word(string_list):
    new_dict = {}
    for item in string_list:
        count = string_list.count(item)
        new_dict[item] = count
    
    return new_dict


given_sentence = input().split()
#print(given_sentence)
word_count_dict= count_word(given_sentence)
result = print_dict(word_count_dict)
