#kSumOfPairs


#Method 1
def get_k_sum_of_pairs(list_num,k):
    set_1 = set()
    pairs = ()
    for i in list_num:
        for j in list_num:
            condition = i + j == k 
            
            if condition == True:
                pair = (i,j)
                sorted_pair = tuple(sorted(pair))
                #print("sorted_pair",sorted_pair)
                set_1.add(sorted_pair)
    return set_1

#Method_2
def get_k_sum_of_pairs_method_2(list_num,k):
    set_1 = set()
    pairs = ()
    stop_index = len(list_num) - 1 #where we don't need to check last element bcz there is no next element for last element
    
    for cur_index in range(stop_index):
        num_1 = list_num[cur_index]
        num_2 = k - num_1
        remaing_list = list_num[cur_index:]
        #check num_2 is present in remaing_list by using membership operator
        if num_2 in remaing_list:
            pairs = (num_1 , num_2)
            sorted_pair = tuple(sorted(pairs))
            set_1.add(sorted_pair)
    return set_1
  

list_num = list(map(int,input().split(",")))
k = int(input())

  
kSumOfPairs_2 = get_k_sum_of_pairs_method_2(list_num,k)

for unique_pairs in kSumOfPairs_2:
    print(unique_pairs)