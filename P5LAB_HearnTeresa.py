#defines the function days_in_feb
def days_in_feb(user_year):
    #takes the year and determines if its a leap year or not.
    if user_year % 4 == 0 and user_year % 100 == 0 and user_year % 400 ==0:
        is_leap_year=True
    elif user_year % 4 == 0 and user_year % 100 != 0:
        is_leap_year=True
    elif user_year % 100 ==00:
        is_leap_year=False
    elif user_year % 400 == 0:
        is_leap_year=True
    else:
        is_leap_year=False
    #after it's determined it was leap year or not it then determines how many days it would be.    
    if is_leap_year==True:
        days=29
    else:
        days=28
    #returns the results     
    return days    
    

if __name__ == '__main__':
    user_input=int(input())
    days_print = days_in_feb(user_input)
    
    print(f'{user_input} has {days_print} days in February.')