#1

from datetime import date, timedelta  

current_date = date.today()  
date_before_5_days = current_date - timedelta(days=5)  

print("Current date:", current_date)  
print("Date 5 days ago:", date_before_5_days)  


#2

from datetime import date, timedelta  

today = date.today()  
yesterday = today - timedelta(days=1)  
tomorrow = today + timedelta(days=1)  

print("Yesterday:", yesterday)  
print("Today:", today)  
print("Tomorrow:", tomorrow)  


#3

from datetime import datetime  

now_with_microseconds = datetime.now()  
now_without_microseconds = now_with_microseconds.replace(microsecond=0)  

print("With microseconds:", now_with_microseconds)  
print("Without microseconds:", now_without_microseconds)  


#4

from datetime import datetime  

current_time = datetime.now()  
fixed_time = datetime.strptime("14 February 2024, 07:00:00", "%d %B %Y, %H:%M:%S")  

time_difference = current_time - fixed_time  
seconds_difference = time_difference.total_seconds()  

print("Current datetime:", current_time)  
print("Difference in seconds:", int(seconds_difference))  

