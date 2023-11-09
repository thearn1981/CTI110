# CTI-110

#  P4HW2 - Salary Calculator

# Teresa Hearn

# Date: 11/08/2023

#




#sets the variables needed for running totals

count=0
total_overtime=0
totalregular=0
totalgross=0

#ask user for name, hours, and employee's rate
print()
print("Enter employee's name or", "'Done' to terminate: ",end='')
emp_name = input()

#Create a while loop that runs as long as Done is not entered
while emp_name != "Done":
    
      
    count=count+1
    
    print("How many hours did " + emp_name + " work? ",end="")
    totalhour = float(input())

    print("What is " + emp_name + "'s pay rate? ",end="")    
    payrate = float(input())
    
    #calculates the pay rate of the current employee's rate
    overtime_rate = payrate * 1.5
        
#takes the current information entered and determines if they worked over time or not. Then proceeds to calculate the results. 
    if totalhour > 40:
        overtime_hours = totalhour - 40
        
        overtime_pay = overtime_hours * overtime_rate
        emp_hours = float(40)
        
        regular_pay = emp_hours * payrate
        
        total_overtime += overtime_pay
        totalregular += regular_pay
        
    else:
        overtime_hours=float(0.00)

        overtime_pay = float(0.00)
        
        regular_pay = totalhour * payrate

        total_overtime += overtime_pay
        totalregular += regular_pay
        



    
    gross_pay = regular_pay + overtime_pay
    
    totalgross += gross_pay

    #Display the results for the current employee.
    print()
    print()
    print(f'\n{"Employee name:":15}{emp_name}\n')
    print(f'{"Hours Worked":15}{"Pay Rate":10}{"OverTime":10}{"OverTime Pay":15}{"RegHour Pay":14}{"Gross Pay"}')
    print("-"*73)
    print(f'{totalhour:<15.1f}{payrate:<10.1f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<0.2f}')
    print()


    #asks user again for input.
    print()
    print("Enter employee's name or", "'Done' to terminate: ",end='')
    emp_name = input()

    

        

#Display the results of the running totals
print()
print()
print(f'{"Total number of employees entered: "}{count}')
print(f'{"Total amount paid for overtime: "}${total_overtime:.2f}')
print(f'{"Total amount paid for regular hours: "}${totalregular:.2f}')
print(f'{"Total amount paid in gross: "}${totalgross:.2f}')




