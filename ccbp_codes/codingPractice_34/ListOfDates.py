#ListOfDates

from datetime import * 

def convert_str_to_date(str_date):
    date_time = datetime.strptime(str_date, "%b %d %Y")
    return date_time

def get_list_of_dates(date_1,date_2):
    difference = date_2 - date_1
    days = difference.days
    #print(days)
    days_list = []
    
    for i in range(days+1):
        delta = timedelta(days = i ) #adding i days as duration 
        new_date = date_1 + delta 
        str_new_date = new_date.strftime("%Y-%m-%d %H:%M:%S") #converting from datetime class to str class by using formatting method
        days_list += [str_new_date]
        
    return days_list
        

given_date_1 = input()
given_date_2 = input()

date_1 = convert_str_to_date(given_date_1)
#print(date_1)
date_2 = convert_str_to_date(given_date_2)
#print(date_2)

dates_list = get_list_of_dates(date_1,date_2)

for date in dates_list:
    print(date)
