#printDates

from datetime import *

def convert_to_date_time(given_string_date):
    date_time = datetime.strptime(given_string_date, "%d %b %Y")
    return date_time

given_string_date = input()
#print(given_string_date)

current_date_time = convert_to_date_time(given_string_date)

delta = timedelta(hours = 24) #USED timedelta class for duration 
prev_day = current_date_time - delta
next_day = current_date_time + delta

print(prev_day)
print(current_date_time)
print(next_day)
