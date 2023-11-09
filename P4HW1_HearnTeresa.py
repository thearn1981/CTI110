# CTI-110

# P4HW1 - Score List

# Teresa Hearn
# 11-6-2023

#The program asks for scores from user then calculates and displays results

fall_scores = []

#asks user for how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))


#used the input from user to make a for loop to create the list of scores 
for num in range (1, num_scores+1):
    
    print("Enter score #",num,":",end =" ")
    score = int(input())

    #validates the score is between 0 and 100
    while score < 0 or score >100:
        #print()
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        print("Enter score # ", num ," again:", end=" ")
               
        score = int(input())

    fall_scores.append(score)

#after calculating the average it then determines which letter grade the score gets.    
average=sum(fall_scores)/len(fall_scores)
if average >90:
    grade = "A"
elif average >=80:
    grade = "B"
elif average >=70:
    grade = "C"
elif average >=60:
    grade = "D"
else:
    grade = "F"

#displays the results of the scores
print(f'\n{"-"*8}{"Results"}{"-"*8}')
print(f'{"Lowest Score":<16}{": "}{min(fall_scores)}')
print(f'{"Modified List":<16}{": "}{fall_scores}')
print(f'{"Scores Average":<16}{": "}{average:.2f}')
print(f'{"Grade":<16}{": "}{grade}')
print(f'{"-"*23}')
