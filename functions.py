
def menu():
    """
    Displays a menu for users to choice from!
    """
    
    
    print("-"*10,"MAIN MENU","-"*10)
    print("1. Adding Random Numbers\n2. Subtracting Random Numbers\n3. Exit\n")
    return



    
def subtract_nums():
    #calculates the answer 
    i=1
    answer = first-second

    #determines which number is bigger and lists that one first so no negative number.
    if first>second:
        answer = first-second
        print(" ",first)
        print("-",second)
        print("-"*8)
    else:
        answer =second-first
        print(" ",second)
        print("-",first)
        print("-"*8)
        
    
    
    user_answer = int(input("Enter answer: "))
#after user gives answer evulates to see if correct or not while keeping count.
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

    
