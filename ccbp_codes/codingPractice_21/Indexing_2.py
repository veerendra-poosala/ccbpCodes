#Indexing_2

def indexing(arg_1, arg_2):
    for i in range(len(arg_1)):
        if i == arg_2:
            break 
    return arg_1[i]

word = input()
index = int(input())

result = indexing(arg_1 = word,arg_2 = index)
print(result)
