#1
from datetime import datetime, timedelta

current_date = datetime.now()
substract_days = current_date - timedelta(days=5)

print(current_date)
print(substract_days)

#2
from datetime import datetime, timedelta

current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print("yesterday:", yesterday.strftime('%Y-%m-%d'))
print("today:", current_date.strftime('%Y-%m-%d'))
print("tomorrow:", tomorrow.strftime('%Y-%m-%d'))

#3
from datetime import datetime

current_time = datetime.now()
drop_microseconds = current_time.replace(microsecond=0)

print(current_time)
print(drop_microseconds)

#4
from datetime import datetime

try:
    date_str1 = input()
    date_str2 = input()
    date1 = datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')

    diff = (date2 - date1).total_seconds()

    print(diff)
except ValueError:
    print("Error")


