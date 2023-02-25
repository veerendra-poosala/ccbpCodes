#CommonElementsInThreeSets

def common_elements_in_three_sets(list_1,list_2,list_3):
    
    list_1 = tuple(sorted(list_1))
    set_1 = set(list_1)

    list_2 = tuple(sorted(list_2))
    set_2 = set(list_2)
    
    list_3 = tuple(sorted(list_3))
    set_3 = set(list_3)
    
    common_elements = set_1 & set_2 & set_3
    common_elements = list(common_elements)
    
    return common_elements


list_1 = list(map(int,input().split()))
list_2 = list(map(int,input().split()))
list_3 = list(map(int,input().split()))

result = common_elements_in_three_sets(list_1,list_2,list_3)
print(result)