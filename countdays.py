import datetime
from datetime import datetime
from datetime import timedelta
import calendar

given_day="Sunday"
given_year=1990
given_month=7
count=0

for m in calendar.monthcalendar(given_year,given_month):
    if m[calendar.SUNDAY]!=0:
        count+=1
print(count)
# print(count)
