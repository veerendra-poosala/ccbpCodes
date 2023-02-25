#NumberGame
from copy import deepcopy 

def play_number_game(total_group,s):
    left_group = total_group[s:]
    right_group = total_group[:-s]
    
    return left_group,right_group

def print_game_result(result):
    for i in range(len(result)):
        row = ""
        for j in range(len(result[i])):
            item = str(result[i][j])
            row += item+" "
        print(row)

def main():
    total_group = list(map(int,input().split(",")))
    s = int(input())
    result = play_number_game(total_group,s)
    print_result = print_game_result(result)
    
main()
