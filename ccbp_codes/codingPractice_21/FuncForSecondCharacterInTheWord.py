#FuncForSecondCharacterInTheWord

def second_character(arg_1):
    
    for i in range(len(arg_1)):
        if i == 1:
            break
    return arg_1[i]

word = input()
result = second_character(word)
print(result)
