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

# Create variables and assign values
print("Welcome to Mr.Euclid's addition quiz!")
strContinue = "y"

# Perform calculations and operations
while strContinue == "y":
    import random
    intNum1 = random.randint(20, 29)
    intNum2 = random.randint(20, 29)
    intAnswer = intNum1 + intNum2
    intResponse = int(input(f"What is the result of {intNum1} + {intNum2}? "))
    while intResponse != intAnswer:
        intResponse = int(input("That is incorrect. Please try again. "))
    print("Correct! Great job.")
    strContinue = input("Would you like to continue the quiz? Please enter 'y' or 'n'. ")
        

# Display output to user
print("Thank you for your participation! Come back to practice anytime. ")

# Add Output of final program as Comments
# ------------------------------------------------------------------
##= RESTART: /Volumes/USB DISK/MCC/ASSIGNMENTS BY SEMESTER/WINTER 2025/COMS-170/program4.py
##Welcome to Mr.Euclid's addition quiz!
##What is the result of 24 + 23? 25
##That is incorrect. Please try again. 25
##That is incorrect. Please try again. 47
##Correct! Great job.
##Would you like to continue the quiz? Please enter 'y' or 'n'. y
##What is the result of 27 + 26? 53
##Correct! Great job.
##Would you like to continue the quiz? Please enter 'y' or 'n'. n
##Thank you for your participation! Come back to practice anytime. 
