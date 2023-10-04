
#Travel budget that subtracts the expenses from the budget and displays the results.
#09/21/2023
#CTI-110
#Teresa Hearn
#


print("This program calculates and displays travel expenses") 
budget=int(input("Enter Budget: "))  #asks user for budget
destination=input("Enter your travel destination: ") #asks user for destination
gasExpense=int(input("How much do you think you will spend on gas? ")) #Asks user for amount to spend on gas
accomodationExpense=int(input("Approximately, how much will you need for accomodation/hotel? ")) #asks user for amount on accomodation
foodExpense=int(input("Last, how much do you need for food? ")) #asks user for how much to spend on food

#displays the input the user entered
print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:",budget,"\n" )
print("Fuel:",gasExpense)
print("Accomodation:",accomodationExpense)
print("Food:",foodExpense,"\n" )


budgetLeft=budget-gasExpense-accomodationExpense-foodExpense #calculates budget left over by subtracting the expenses from the starting budget
print("Remaining Balance:",budgetLeft) #prints the results

