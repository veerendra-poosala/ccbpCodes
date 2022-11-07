#SetRelation

def set_relation(set_1,set_2):
    is_superset =  set_1.issuperset(set_2)
    is_subset = set_1.issubset(set_2)
    is_disjoint = set_1.isdisjoint(set_2)
    
    if is_superset == True:
        return "Superset"
    elif is_subset == True:
        return "Subset"
    elif is_disjoint == True:
        return "Disjoint Set"


num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here

int_list = list(map(int,input().split()))
new_list = tuple(sorted(int_list))
new_set = set(new_list)

result = set_relation(set_1 = num_set,set_2 = new_set)
print(result)
