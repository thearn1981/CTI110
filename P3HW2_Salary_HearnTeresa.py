# CTI-110

# P3HW2 - Salary

# Teresa Hearn

# Date: 10/23/2023

#

#ask user for name, hours, and employee's rate

emp_name = input("Enter employee's name: ")
emp_totalhours = float(input("Enter number of hours worked: "))
emp_payrate = float(input("Enter employee's pay rate: "))

#determine if overtime
overtime_rate = emp_payrate * 1.5

if emp_totalhours > 40:
    overtime_hours = emp_totalhours - 40
    overtime_pay = overtime_hours * overtime_rate
    emp_hours = float(40)
    regular_pay = emp_hours * emp_payrate
    
else:
    overtime_hours = float(0.00)
    overtime_pay = float(0.00)
    regular_pay = emp_totalhours * emp_payrate

#determine Regular hour pay and gross pay

#regular_pay = emp_hours * emp_payrate
gross_pay = regular_pay + overtime_pay

#Display the results 
print("-"*40)
print(f'{"Employee name:":15}{emp_name}\n')
print(f'{"Hours Worked":<15}{"Pay Rate":12}{"OverTime":12}{"OverTime Pay":<17}{"RegHour Pay":<17}{"Gross Pay":}')
print("-"*40)
print(f'{emp_totalhours:<15.1f}{emp_payrate:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<17.2f}${regular_pay:<12.2f}${gross_pay:<.2f}\n')
print("-"*40)
