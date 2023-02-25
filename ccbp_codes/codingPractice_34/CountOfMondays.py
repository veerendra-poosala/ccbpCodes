#CountOfMondays

from datetime import *

def convert_str_to_date(str_date):
    date_time = datetime.strptime(str_date, "%Y")
    return date_time

def get_count_of_given_weekday(year_1,year_2,weekday_name = "Monday"):
    
    difference = year_2 - year_1
    #print(difference)
    #print(type(difference))
    days = difference.days + 365 #where adding 365 because checking weekday_name in year_2 also
    
    week_days_list = []
    
    
    for i in range(days+1):
        delta = timedelta(days = i)
        new_date = year_1 + delta
        f_date = new_date.strftime("%d") #getting date
        f_weekday = new_date.strftime("%A") #getting weekday name , formatted weekday
        f_year = new_date.strftime("%Y")   #updated year 
        
        f_year_2 = year_2.strftime("%Y") #given year
        
        
        if f_weekday == weekday_name and int(f_date) == 1 and (int(f_year) <= int(f_year_2) ) :
            f_new_date = new_date.strftime("%Y-%m-%d")
            week_days_list += [f_new_date]
        
        if i == days:
            f_new_date = new_date.strftime("%Y-%m-%d")
            last_date = f_new_date #just for testing which date is lastdate
            #print(last_date)
            
    count = len(week_days_list)
    
    return count
    

str_year1,str_year2 = input().split()


year_1 = convert_str_to_date(str_year1)
#print(year_1)
year_2 = convert_str_to_date(str_year2)
#print(year_2)
count_of_mondays = get_count_of_given_weekday(year_1,year_2,"Monday")
print(count_of_mondays)