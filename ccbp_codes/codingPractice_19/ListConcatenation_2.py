#ListConcatenation_2

terms_n = int(input())

new_list = []

for i in range(terms_n):
    given_input = input()
    condition_1 = i >=0 and i <=2
    condtion_2 = i >= (terms_n-3) and i <= (terms_n)
    if condition_1 or condtion_2 :
        new_list += [given_input]
print(new_list)