
#Travel budget that subtracts the expenses from the budget and displays the results.
#09/21/2023
#CTI-110
#Teresa Hearn
#


#Asking the user for input for budget, gas expense, accomodation expense, and food expense

print("This program calculates and displays travel expenses")
budget=int(input("Enter Budget:"))
destination=input("Enter your travel destination:")
gasExpense=int(input("How much do you think you will spend on gas?"))
accomodationExpense=int(input("Approximately, how much will you need for accomodation/hotel?"))
foodExpense=int(input("Last, how much do you need for food?"))

#displays the input the user entered
print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:",budget,"\n" )

print("Fuel:",gasExpense)
print("Accomodation:",accomodationExpense)
print("Food:",foodExpense,"\n" )


#calculates budget left over after the other expenses and prints the results.

budgetLeft=budget-gasExpense-accomodationExpense-foodExpense
print("Remaining Balance:",budgetLeft)

