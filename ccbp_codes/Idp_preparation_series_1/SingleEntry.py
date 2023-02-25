#SingleEntry

def get_single_entry_fr_list(num_list):
    resultant_num = None
    for i in range(len(num_list)):
        num = num_list[i]
        count = num_list.count(num)
        if count == 1:
            resultant_num = num
    return resultant_num
        
def main():
    num_list = list(map(int,input().split()))
    result = get_single_entry_fr_list(num_list)
    print(result)
main()