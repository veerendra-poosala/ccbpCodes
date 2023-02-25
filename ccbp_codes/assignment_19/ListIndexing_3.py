#ListIndexing_3 

terms_n = int(input())
testcases_t = int(input())
new_list = []

for i in range(terms_n):
    
    n = int(input())
    new_list += [n]

#print(new_list)

for t in range(testcases_t):
    index_k = int(input())
    
    print(new_list[index_k])