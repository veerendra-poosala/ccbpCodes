#MathQuiz

def find_sum_of_given_range_list(numbers_list,start,end):
    
    items = list(range(start,end+1))
    total = 0 
    for num in numbers_list:
        for item in items:
            if num == item:
                total += num
    return total
    
def main():
    numbers_list = list(map(int,input().split()))
    m = int(input())
    for i in range(m):
        start,end  = map(int,input().split()) 
        sum_of_given_range = find_sum_of_given_range_list(numbers_list,start,end)
        print(sum_of_given_range)
main()