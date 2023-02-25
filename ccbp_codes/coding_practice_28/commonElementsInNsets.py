#commonElementsInNsets

def common_elements_in_n_sets(n,list_n):
    if n <= 0 :
        return sorted(list_n)
        
    first_list = tuple(sorted(list_n ))
    first_set = set(first_list)

    #getting inputs from user
    second_list = list(map(int,input().split()))
    second_list = tuple(sorted(second_list))
    second_set = set(second_list)
    
    #checking common elements 
    common_elements = first_set & second_set
    common_elements = list(common_elements)
    
    if n == 1:
        return sorted(common_elements)
    
    return common_elements_in_n_sets(n-1,common_elements)
    
    


n = int(input())
first_list = list(map(int,input().split()))
x = n -1 
result = common_elements_in_n_sets(n = x,list_n = first_list)
print(result)
