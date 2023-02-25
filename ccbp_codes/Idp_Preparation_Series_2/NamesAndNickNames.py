#NamesAndNicknames

def check_names_list(names_list):
    msg = "No"
    for name_1 in names_list:
        count = names_list.count(name_1)
        if count > 1:
            msg = "Yes"
            return msg
    return msg
    
def get_names_list(n):
    names_list = []
    for i in range(n):
        name = input().split()
        names_list.append(name)
    return names_list

def main():
    no_of_sets = int(input())
    for set_i in range(no_of_sets):
        n = int(input())
        names_list = get_names_list(n)
        is_name_and_nickname_same = check_names_list(names_list)
        print(is_name_and_nickname_same)
main()