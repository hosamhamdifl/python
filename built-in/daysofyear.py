def is_year_leap(year):
    if year % 4 != 0:
            return False
    elif year % 100 != 0:
            return True 
    elif year % 400 != 0:
            return False 
    else:
            return True 
def days_in_month(year, month):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
        
    if is_year_leap(year):
        days[1]=29
       
    return days[month-1]

def day_of_year(year, month, day):
    d=0
    for i in range(month):
       d+=days_in_month(year,i) 
    return d
    

print(day_of_year(2003, 12, 31))
