def is_year_leap(year):
#
    return year%4 ==0 and (year%100 ==0 and year%400 ==0 ) or year%4 ==0 and (not year%100 ==0 and not year%400 ==0 )
#

def days_in_month(year, month):
    meses30 = [11,4,6,9]
    meses31 = [1,3,5,7,8,10,12]
#
    if month not in meses30 and month not in meses31 and month !=2:
        #print ("None")
        return None
    else:
        #print(month)
        if month == 2:
            #print("febrero")
            if is_year_leap(year):
                #print ("tiene 29")
                return 29
            else:
            #print ("tiene 28")
                return 28
        elif month in meses30:
            #print ("tiene 30")
            return 30
        else:
            #print ("tiene 31")
            return 31



test_years = [1900, 2000, 2016, 1987, 1987]
test_months = [2, 2, 1, 11,13]
test_results = [28, 29, 31, 30,None]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")