#swapCharacters
from copy import deepcopy
def compare_two_strings(s,t):
    s_list = list(s)
    t_list = list(t)

    start = 0
    while True:
        c_list = deepcopy(s_list)
        for i in range(start,len(s_list)):
            temp = c_list[i]
            c_list[i] = c_list[-1]
            c_list[-1] = temp
            condintion = c_list == t_list
            if condintion == True:
                return condintion
            print(c_list,t_list)
        print("start",start)
        if start > len(c_list):
            break
        start += 1
    return condintion

def main():
    s =input()
    t =input()
    s = s.lower()
    t = t.lower()

    swap_result = compare_two_strings(s,t)

    if swap_result or s == t:
        print("Yes")
    else:
        print("No")

main()