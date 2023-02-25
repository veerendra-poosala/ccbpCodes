#HungerGames_II


def play_game(data):
    no_of_players = data[0]
    players_list = list(range(1,no_of_players+1))
    #print(players_list)
    no_of_chocolates = data[1]
    starting_point = data[2]
    counter = 0
    i = starting_point
    while counter < no_of_chocolates:
        player = players_list[i-1]
        #print("player",player,i)
        if i == len(players_list):
            i = 0
        i += 1 
        counter += 1
    return player
    

def main():
    no_of_rounds = int(input())
    for round_i in range(no_of_rounds):
        round_i_data = list(map(int,input().split()))
        round_winner = play_game(round_i_data)
        print(round_winner)
main()
