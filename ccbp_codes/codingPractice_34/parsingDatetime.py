from datetime import datetime

def parsing_datetime(given_date):
    date_obj = datetime.strptime(given_date, "%d %b %Y")
    print(date_obj)

given_date = input()
#print(given_date)
res = parsing_datetime(given_date)
