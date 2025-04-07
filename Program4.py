# Madison Cronk
# 0582982
# Program # 4
# COMS-170-01: Winter 2025
# Due: 2/28/2025
# Program #4 - Create a program to act as an addition quiz for Mr.Euclid. 
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# strContinue           string      holds the user response indicating to continue or end the quiz
# intNum1               integer     randomly generated value number 1
# intNum2               integer     randomly generated value number 2
# intResponse           integer     user response to the generated addition equation
# intAnswer             integer     stores the value of the correct answer to the given equation

import random

# Create variables and assign values
print("Welcome to Mr.Euclid's addition quiz!")
strContinue = "y"

# Perform calculations and operations
while strContinue == "y":
    intNum1 = random.randint(20, 29)
    intNum2 = random.randint(20, 29)
    intAnswer = intNum1 + intNum2
    intResponse = int(input(f"What is the result of {intNum1} + {intNum2}? "))
    if intResponse == intAnswer:
        print("Correct! Great job.")
    else:
        print(f"That is incorrect. The correct answer is {intAnswer}.")
    strContinue = input("Would you like to continue the quiz? Please enter 'y' or 'n'. ")
# Display output to user
while strContinue != 'y':
    print("Thank you for your participation! Come back to practice anytime. ")
while strContinue is not ['y','n']:
    print("ERROR - Please enter a valid menu option")

