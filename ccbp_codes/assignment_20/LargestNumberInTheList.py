#LargestNumberInTheList

given_list = input().split()

ref_num = int(given_list[0])

for num in given_list:
    num = int(num)
    
    if num >= ref_num :
        ref_num = num
    else:
        ref_num = ref_num
print(ref_num)