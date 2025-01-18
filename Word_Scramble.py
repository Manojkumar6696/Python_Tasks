#To use random function we are importing 
import random

#Creating list with words

Words=['python','javascript','java','automation','pytest','guvi','selenium']

#Assigning random numbers in variable and also assigning Words in randon function 

Guess_Words=random.randint(0,6)

#Using the random number in the Words list to get the random words

Random_Words=Words[Guess_Words]  


while True:
#To get input from user we are using input function and assigning the values in variable
    User_input=input()

#Using conditional statement to check the user input
    if (User_input==Random_Words):
        print("Bravo You Found a Correct Word: "+ User_input +"!")
    else:
        print("Better Luck Next Time")
    
