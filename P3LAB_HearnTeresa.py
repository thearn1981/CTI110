
is_leap_year = False

#asks user for year to check   
input_year = int(input())

#determines if the year entered is leap year or not
if input_year % 4 == 0 and input_year % 100 == 0 and input_year % 400 ==0:
    is_leap_year=True
elif input_year % 4 == 0 and input_year % 100 != 0:
    is_leap_year=True
elif input_year % 100 ==00:
    is_leap_year=False
elif input_year % 400 == 0:
    is_leap_year=True
else:
    is_leap_year=False
#prints the results   
if is_leap_year==True:
    print(f'{input_year} - leap year')
else:
    
    print(f'{input_year} - not a leap year')
