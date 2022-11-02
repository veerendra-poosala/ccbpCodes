#ReverseTheSentence

given_list = input().split()
#print(given_list)
new_list = []

for item in given_list:
    new_list = [item] + new_list
#print(new_list)
result_string = " ".join(new_list)
print(result_string)