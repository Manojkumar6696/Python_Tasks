#To use random function we are importing 
import random

#Assigning random numbers in variable and also using predefined randint function to mention it as we are using integer numbers for this game 

Guess_Number=random.randint(1,1000)

#Using While loop to check the user condition

while True:
#To get input from user we are using input function and assigning the values in variable
    User_input=int(input())

#Using conditional statement to check the user input with auto generated number
    if (User_input>Guess_Number):
        print("Guess is too High!")
    
    elif (User_input<Guess_Number):
        print("Guess is too Low!")
    
    else:
        print("Bravo Correct Guess!")

