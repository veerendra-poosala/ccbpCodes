#nthNumberSum

def perform_nth_number_sum(numbers_list,range_list,n):
    nth_sum = 0 
    start = n
    end = range_list[-1]
    for i in range(len(numbers_list)):
        val = numbers_list[i]
        range_val = 0
        if i < len(range_list):
            range_val = range_list[i]
        #print("range_val",range_val,"i",i,"start",start,"val",val)
        if range_val % start == 0 :
            #print("val",val)
            nth_sum += val
    return nth_sum

def main():
    n,m = map(int,input().split())
    numbers_list = list(map(int,input().split()))
    range_list = list(range(1,m+1))
    #print(range_list)
    result = perform_nth_number_sum(numbers_list,range_list,n)
    print(result)

main()