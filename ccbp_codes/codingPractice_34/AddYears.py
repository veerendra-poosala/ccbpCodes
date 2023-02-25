#AddYears

from datetime import * 

def convert_str_to_date(given_date):
    date_time = datetime.strptime(given_date, "%b %d %Y")
    return date_time

def get_new_date(current_date,years_n):
    add_days = 365 * years_n
    delta = timedelta(days=add_days)
    new_date = current_date + delta
    return new_date
    

given_date = input()
years_n = int(input())

current_date = convert_str_to_date(given_date)
#print(current_date)
res = get_new_date(current_date,years_n)
print(res)