#IPLMatchDetails

#win = 3 points, loss = 0, draw = 1
#Matches Played
#Matches Won
#Matches Drawn
#Matches Lost
#Points 

def print_summary_dict(summary_dict):
    
    match_points_list = []
    for val in summary_dict.values():
        match_points_list.append(val[4])
    match_points_list= sorted(match_points_list, reverse = True)
    #print("match_points_list",match_points_list)
    
    items_list = list(summary_dict.items())
    #print("items_list:",items_list)
    #print(items_list[0][1][4])
    
    for val in match_points_list:
        msg = "Team: {}, Matches Played: {}, Won: {}, Lost: {}, Draw: {}, Points: {}"
        for i in range(len(items_list)):
            item = items_list[i]
            points = item[1][4]
            #print("val",val,"item",item,"p",points)
            if val == points:
                key = item[0]
                mp = item[1][0]
                wins = item[1][1]
                lost = item[1][2]
                draw = item[1][3]
                msg = msg.format(key,mp,wins,lost,draw,points)
                print(msg)
                break
     

def get_summary_dict(summary_list):
    summary_dict = {}
    for item in summary_list:
        team_1_name = item[0]
        team_2_name = item[1]
        t1_played = 1 
        t2_played = 1
        t1_wins = 0 
        t2_wins = 0 
        t1_loss = 0
        t2_loss = 0
        t1_draw = 0
        t2_draw = 0
        if item[2] == "loss":
            team_1_points = 0 
            team_2_points = 3
            t1_loss = 1
            t2_wins = 1
        elif item[2] == "win":
            team_1_points = 3 
            team_2_points = 0
            t1_wins = 1
            t2_loss = 1
            
        elif item[2] == "draw":
            team_1_points = 1 
            team_2_points = 1 
            t1_draw = 1
            t2_draw = 1
        #checking team name is already existing or not. if exists updates the new value with old value
        if team_1_name in summary_dict:
            prev_values = summary_dict[team_1_name]
            t1_played = prev_values[0] + t1_played
            t1_wins = prev_values[1] + t1_wins
            t1_loss = prev_values[2] + t1_loss
            t1_draw = prev_values[3] + t1_draw
            team_1_points = prev_values[4] + team_1_points
        if team_2_name in summary_dict:
            prev_values = summary_dict[team_2_name]
            t2_played = prev_values[0] + t2_played
            t2_wins = prev_values[1] + t2_wins
            t2_loss = prev_values[2] + t2_loss
            t2_draw = prev_values[3] + t2_draw
            team_2_points = prev_values[4] + team_2_points
        summary_dict[team_1_name] = [t1_played, t1_wins, t1_loss, t1_draw, team_1_points]
        summary_dict[team_2_name] = [t2_played, t2_wins, t2_loss, t2_draw, team_2_points]
    return summary_dict
            

def get_summay_list(n=0,res_list=[]):
    summary_list = res_list
    row_list = input().split(";")
    summary_list.append(row_list)
    if n <= 1:
        return summary_list
    return get_summay_list(n=n-1,res_list=summary_list)


n = int(input())
summary_list = []
if n==0:
    print("No Output")
elif  n >= 0 and n <= 100:
    summary_list = get_summay_list(n)
    summary_dict = get_summary_dict(summary_list)
    print_summary = print_summary_dict(summary_dict)
    