#NewYearCountdown

from datetime import *

def convert_str_to_date(str_date):
    date_time = datetime.strptime(str_date, "%b %d %Y %I:%M %p")
    return date_time

def get_nearest_new_year(date):

    nxt_year = date.strftime("%Y")
    nxt_year = int(nxt_year) + 1
    nearest_new_year = datetime(nxt_year, 1, 1, 0, 0, 0)
    
    differnce = nearest_new_year - date
    days = differnce.days
    seconds = differnce.seconds
    hours = seconds / 3600
    hours = int(hours)
    seconds = seconds % 3600
    minutes = seconds / 60
    minutes = int(minutes)
    total_hours = (days * 24)+hours
    
    msg = "{} hours {} minutes".format(total_hours,minutes)
    return msg
    

str_date = input()

date = convert_str_to_date(str_date)
#print(date)
nearest_new_year = get_nearest_new_year(date)
print(nearest_new_year)
