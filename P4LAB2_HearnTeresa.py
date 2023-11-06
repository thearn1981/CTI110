#asks user for inputs
one = int(input())
two=int(input())

#determine if second number is larger then first
if two < one:
    print("Second integer can't be less than the first.")
else:
    
    for num in range(one, two+1, 5):
        print(num, end= " ")
    print()