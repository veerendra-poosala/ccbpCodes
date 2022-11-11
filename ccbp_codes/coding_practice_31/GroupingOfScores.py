#GroupingOfScores

def grouping_of_score(balls_scores_list):
    new_dict = {}
    
    for ball_details in balls_scores_list:
        each_ball_details_list = ball_details.split(":")
        ball_color,ball_score = each_ball_details_list[0],int(each_ball_details_list[1])
        
        if ball_color in new_dict:
            score = new_dict[ball_color]
            total_score = score + ball_score
            new_dict[ball_color] = total_score 
        else:
            new_dict[ball_color] = ball_score
    
    return new_dict
        
    
    
balls_scores_list = input().split(",")
#print(given_list_of_score)

result_dict = grouping_of_score(balls_scores_list)
result_list = list(result_dict.items())

print(sorted(result_list))
