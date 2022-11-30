#FormattingDatetime

from datetime import datetime

def format_datetime(given_date):
    
    formatted_datetime_1 = datetime.strptime(given_date, "%b %d %Y %I:%M%p") #date parsing method
    #print(formatted_datetime_1)
    formatted_datetime_2 = formatted_datetime_1.strftime("%d/%m/%Y %H:%M:%S") #format method
    print(formatted_datetime_2)
given_date = input()
#print(given_date)

res = format_datetime(given_date)