
#Travel budget that calculates what would be left of a budget.
#10/7/2023
# CTI-110 P2HW1 - Travel
#Teresa Hearn
#


print("This program calculates and displays travel expenses\n")
#Asks user for input related to the budget
budget=float(input("Enter Budget: "))
print()
destination=input("Enter your travel destination: ")
print()
gasExpense=float(input("How much do you think you will spend on gas? "))
print()
accomodationExpense=float(input("Approximately, how much will you need for accomodation/hotel? ")) 
print()
foodExpense=float(input("Last, how much do you need for food? ")) 

#displays the input the user entered
print("\n------------Travel Expenses------------")
print(f'{"Location:":20}{destination}')
print(f'{"Initial Budget:":20}${budget:.1f}' )
print(f'{"Fuel:":20}${gasExpense:.1f}')
print(f'{"Accomodation:":20}${accomodationExpense:.1f}')
print(f'{"Food:":20}${foodExpense:.1f}' )

#Subtracting the expenses from the budget
budgetLeft=budget-(gasExpense+accomodationExpense+foodExpense) 

#print the results
print("---------------------------------------\n")
print(f'{"Remaining Balance":20}${budgetLeft:.1f}')

