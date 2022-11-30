#UNIXTimestampToDateTime

from datetime import *



def con_unix_timestamp_to_datetime(unix_stamp_u):
    #converting given seconds into days
    days = unix_stamp_u / 86400 # 1 day = 86400 seconds
    #print(days)
    
    #byusing timedelta we can get duration
    delta = timedelta(days=days)
    #print(delta)
    
    #as mentioned in problem ref_date = January 1st, 1970
    ref_date = datetime(1970,1,1,0,0,0 )
    #print(ref_date)
    
    #getting result date by adding duration to the reference date
    new_date = ref_date + delta
    
    return new_date
    

unix_stamp_u = int(input())
#print(unix_stamp_u)

res_date = con_unix_timestamp_to_datetime(unix_stamp_u)
print(res_date)





