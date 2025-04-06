# Madison Cronk
# 0582982
# Program #6
# COMS-170-01: Winter 2025
# Due: 04/04/2025
# Program # 6 - Write a program designed to read a provided file in order to help calculate total sales and average sale price for Dylan's side hustle selling Pokemon cards. 
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# floatAvgSales         float       average sale price as calculated by accumulated sales divided by total amount of sales
# floatGrTotal          float       grant total of accumulated sales
# strChoice             string      placeholder for user inputted chocie from main menu 

def main():
    strChoice = "GO"
    while strChoice != "X":
        print("----------------------------------------------")
        print("         Pokemon Card Sales Main Menu         ")
        print("----------------------------------------------")
        print("Please enter a selection from the menu below:")
        print("D: DISPLAY SALES")
        print("C: CALCULATE TOTAL AND EVERAGE")
        print("X: EXIT THE APPLICATION")

        strChoice = input("Enter your selection: ").upper()

        if strChoice == "D":
            display_card_sales()
        elif strChoice == "C":
            print("----------------------------------------------")
            print("    Calculating total and average sales...    ")
            print("----------------------------------------------")
            floatGrTotal, floatAvgSales = calc_total()
            print(f"Total sales are: ${floatGrTotal:.2f}")
            print(f"Average sales are: ${floatAvgSales:.2f}")
        elif strChoice not in ["D","C","X"]:
            print(ERROR: INVALID SELECTION. PLEASE TRY AGAIN!")
            continue
        else:
            print("See you next time!")
            
def display_card_sales():
    try:
        card_sales = open("cards.txt", "r")
    except FileNotFoundError:
        print("Error: The file cards.txt was not found.")
        return main()
    else: 
        linenumber = 1
        for line in card_sales:
            line = line.strip()
            print(linenumber, ":", line)
            linenumber += 1
    card_sales.close()   

def calc_total():
    try:
        card_sales = open("cards.txt", "r")
    except FileNotFoundError:
            print("Error: The file cards.txt was not found.")
            return main()
    except ValueError:
        print("Error: The file cards.txt contains invalid data.")
        return main()
    else:
        floatGrTotal = 0
        linecount = 0
        for line in card_sales:
            floatGrTotal += float(line.strip())
            linecount += 1
        card_sales.close()
        if linecount > 0:
            floatAvgSales = floatGrTotal / linecount
        else:
            floatAvgSales = 0
        return floatGrTotal, floatAvgSales

main()
