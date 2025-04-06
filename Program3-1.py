# Madison Cronk
# 0582982
# Program #3
# COMS-170-01: Winter 2025
# Due: 02/07/2025
# Program #3 - Classify students based on credits completed entered as input. 
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
#intCredits             integer     stores the number of completed credits as entered by user

# Create variables and assign values
intCredits = int(input("Enter number of credits completed:"))


# Perform calculations and operations
if intCredits < 0:
    print("ERROR: Negative credits entered")
elif intCredits > 0 and intCredits < 30:
    print("FRESHMAN: Welcome to MUCSOCS")
elif intCredits > 30 and intCredits < 60:
    print("SOPHOMORE: You're making progress")
elif intCredits > 60 and intCredits < 90:
    print("JUNIOR: Getting close. Don't give up now.")
elif intCredits > 90 and intCredits < 120:
    print("SENIOR: Almost done!")
elif intCredits > 120:
    print("Welcome to MUCSOCS Alumni Association")
# Display output to user


# Add Output of final program as Comments
##=================== RESTART: /Users/mads/Desktop/Program3.py ===================
##Enter number of credits completed:118
##SENIOR: Almost done!
##=================== RESTART: /Users/mads/Desktop/Program3.py ===================
##Enter number of credits completed:81
##JUNIOR: Getting close. Don't give up now.
