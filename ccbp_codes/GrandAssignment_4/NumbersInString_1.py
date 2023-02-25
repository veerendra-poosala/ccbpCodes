#NumbersInString_1

def get_sum_and_avg_of_nums_in_str(given_string):
    num_list = []
    length_of_chars = len(given_string)
    for char in given_string:
        if char.isdigit():
            num = int(char)
            num_list.append(num)
            
    total = sum(num_list)
    length_of_nums = len(num_list)
    avg = round((total / length_of_nums),2)
    print(total)
    print(avg)

given_string = input()

result = get_sum_and_avg_of_nums_in_str(given_string)
