#NameOfTheWeekDay

from datetime import * 

def convert_str_to_date_time(given_date):
    date_time = datetime.strptime(given_date,"%d %b %Y")
    return date_time

def get_name_of_the_weekday(date):
    f_date = date.strftime( "%A") #getting weekday name by using date formatting method
    return f_date

given_date = input()

date = convert_str_to_date_time(given_date)
#print(date)
name_of_the_weekday = get_name_of_the_weekday(date)
print(name_of_the_weekday)