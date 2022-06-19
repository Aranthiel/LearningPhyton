def is_year_leap(year):
#
    return year%4 ==0 and (year%100 ==0 and year%400 ==0 ) or year%4 ==0 and (not year%100 ==0 and not year%400 ==0 )
#

def days_in_month(year, month):
    meses30 = [11,4,6,9]
    meses31 = [1,3,5,7,8,10,12]
#
    if month not in meses30 and month not in meses31 and month !=2:
        return None
    else:
        if month == 2:
            if is_year_leap(year):
                return 29
            else:
                return 28
        elif month in meses30:
            return 30
        else:
            return 31

def day_of_year(year, month, day):
    doy =0
    for i in range(1, month):
        doy += days_in_month(year, i)
    return doy+day
#
# Escribe tu código nuevo aquí.
#

print(day_of_year(2000, 1, 25))
print(day_of_year(2000, 2, 25))
print(day_of_year(2000, 3, 1))
print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 1, 25))
print(day_of_year(2001, 2, 25))
print(day_of_year(2001, 3, 1))
print(day_of_year(2001, 12, 31))
