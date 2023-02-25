#RepeatedDigits

def get_count_of_repeated_digits_in_str_num(str_num):
    digit_list = list(str_num)
    rep_digits_list = []
    for digit in digit_list:
        count = digit_list.count(digit)
        if count > 1 and digit not in rep_digits_list:
            rep_digits_list.append(digit)
    rep =len(rep_digits_list)
    return rep
def main():
    num = input()
    count_of_repeated_digits = get_count_of_repeated_digits_in_str_num(num)
    print(count_of_repeated_digits)
main()

