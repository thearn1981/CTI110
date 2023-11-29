   # Math Quiz with menu

   # Date: 11/27/2023

   # CTI-110 P5HW - Math Quiz

   # Teresa Hearn
   #

import random 
import functions as fn



def addition_nums():
    """
    calculates the sum and then displays it for user to add together while keep track of each guess.
    """
    
    i=1
    first=random.randint(100, 999)
    second=random.randint(100, 999)
    answer = first+second
    print(f' {first:.>3}')
    print(f'+{second:.>3}')
    print("-"*8)
    
    user_answer = float(input("Enter answer: "))

    #determines whether or not the answer is correct.
    while user_answer != answer:
        
        #Determines which answer to give to user. 
        i=i+1
        if user_answer > answer:
            print("Sorry, Guess is too high. Try Again!")
            user_answer = int(input("Enter answer: "))
        elif user_answer < answer:
            print("Sorry, Guess is too low. Try Again!")
            user_answer = int(input("Enter answer: "))
    #once answer is correct congratulates user and announces how many attempts.        
    print("\nCongratulations!!!! Your answer is correct!")
    print("number of attempts: ",i)
    return

def subtract_nums():
    """
    Takes two random numbers and presents it to user to solve an subtraction problem. 
    """
    
    i=1
    first=random.randint(100, 999)
    second=random.randint(100, 999)    
    answer = first-second

    #determines which number is bigger and lists that one first.
    if first>second:
        answer = first-second
        print(f' {first:.>3}')
        print(f'-{second:.>3}')
        print("-"*8)
    else:
        answer =second-first
        print(f' {second:.>3}')
        print(f'-{first:.>3}')
        print("-"*8)
        
    
    
    user_answer = float(input("Enter answer: "))
    while user_answer != answer:
        
        
        i=i+1
        if user_answer > answer:
            print("\nSorry, Guess is too high. Try Again!")
            user_answer = int(input("Enter answer: "))
        elif user_answer < answer:
            print("\nSorry, Guess is too low. Try Again!")
            user_answer = int(input("Enter answer: "))
    print("\nCongratulations!!!! Your answer is correct!")
    print("number of attempts: ",i)
    
    
    return 

def main():

    #presents and runs a descision loop to determine which option is selected

    option=0
    print("-"*30)
    print(f'\n{"Welcome to Math Quiz!":>25}\n')
    print("-"*30,"\n\n")
    
    while option != 3:
        
        fn.menu()
        option=int(input("Please choose one of the menu options: ")) 
        if option == 1:

            addition_nums()

        elif option == 2:               
                        
            subtract_nums()

        elif option ==3:
            print("\nThank you for playing!!")
            print("Bye!")
        else:
            print("\nWrong Selection!\nPlease Pick a selection on the menu!\n")

main()
