#TeamPoints

def calculate_league_points(wins, draws, losses):
    each_win = 4 
    each_draw = 2 
    each_loss = -1
    winning_points = each_win * wins
    draw_pints = each_draw * draws
    loss_points = each_loss * losses
    total_points = winning_points + draw_pints + loss_points
    return total_points


statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])

result = calculate_league_points(wins,draws,losses)
print(result)
