#HighestSumOfScores

def find_highest_marks_scored_group(total_groups_list):
    total = 0
    resultant_list = []
    for item in total_groups_list:
        sum_of_marks = sum(item)
        if sum_of_marks > total:
            total = sum_of_marks
            resultant_list = item
    return resultant_list

def print_result(num_list):
    result = ''
    for item in num_list:
        item = str(item)
        result += item + " "
    print(result)
def main():
    no_of_groups = int(input())
    total_groups_list = []
    for i in range(no_of_groups):
        group_list = list(map(int,input().split(",")))
        #total = sum(group_scores_record)
        total_groups_list.append(group_list)
    
    resultant_list = find_highest_marks_scored_group(total_groups_list)
    print_result(resultant_list)

main()