# Madison Cronk
# 0582982
# Program #5
# COMS-170-01: Winter 2025
# Due: 03/21/2025
# Program 5 - Create an application that calculates the final price of various coffee drinks at the new cafe in town, The Coffee Connection
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# floatSubtotal         float       pre-tax price of chosen drink based off display menu
# floatTotalTax         float       total amount of sales tax to be charged on chosen drink
# floatTotal            float       final price of chosen drink after tax
# strChoice             string      user input determining which menu option from main menu to execute
# strCoffee             string      user selected drink they would like to buy, this is what we will be calculating the final price of

def main():
    strChoice = "GO"
    while strChoice != "X":
        print("=====================================================")
        print("*                The Coffee Connection              *")
        print("=====================================================")
        print("Enter an option:")
        print("C. Calculate price for coffee drink being ordered")
        print("D. Display Coffee menu price information")
        print("X. Exit")

        strChoice = input("ENTER YOUR MENU SELECTION:").upper()
        
        if strChoice == "C":
            floatTotal = calc_total()
            print(f"TOTAL PRICE: ${floatTotal:.2f}")
        elif strChoice == "D":
            display_menu()
        

def display_menu():
    print("=====================================================")
    print("*           The Coffee Connection Menu              *")
    print("=====================================================")
    print("ALL PRICES BEFORE TAX")
    print(" ")
    print("BLACK COFFEE: $1.59")
    print("CAPPUCCINO: $3.79")
    print("LATTE: $2.99")
    print("MOCHA LATTE: $3.59")
    print("SHOT OF ESPRESSO: $1.99")
    print(" ")
    print("NOW RETURNING TO MENU")


def calc_tax(floatSubtotal):
    return floatSubtotal * 0.07

def calc_total():
    strCoffee = input("ENTER THE COFFEE DRINK YOU WOULD LIKE TO ORDER: (B)lack Coffee, (C)appuccino, (L)atte, (M)ocha Latte, (S)hot of Espresso:").upper()
    if strCoffee == "B":
        floatSubtotal = 1.59
    elif strCoffee == "C":
        floatSubtotal = 3.79
    elif strCoffee == "L":
        floatSubtotal = 2.99
    elif strCoffee == "M":
        floatSubtotal = 3.59
    elif strCoffee == "S":
        floatSubtotal = 1.99
    else:
        print("INVALID SELECTION!")
        return calc_total()
    floatTotalTax = calc_tax(floatSubtotal)
    return floatSubtotal + floatTotalTax


main()

    

# Add Output of final program as Comments
##================= RESTART: /Users/mads/Desktop/Program5 copy.py ================
##=====================================================
##*                The Coffee Connection              *
##=====================================================
##Enter an option:
##C. Calculate price for coffee drink being ordered
##D. Display Coffee menu price information
##X. Exit
##ENTER YOUR MENU SELECTION:d
##=====================================================
##*           The Coffee Connection Menu              *
##=====================================================
##ALL PRICES BEFORE TAX
## 
##BLACK COFFEE: $1.59
##CAPPUCCINO: $3.79
##LATTE: $2.99
##MOCHA LATTE: $3.59
##SHOT OF ESPRESSO: $1.99
## 
##NOW RETURNING TO MENU
##=====================================================
##*                The Coffee Connection              *
##=====================================================
##Enter an option:
##C. Calculate price for coffee drink being ordered
##D. Display Coffee menu price information
##X. Exit
##ENTER YOUR MENU SELECTION:c
##ENTER THE COFFEE DRINK YOU WOULD LIKE TO ORDER: (B)lack Coffee, (C)appuccino, (L)atte, (M)ocha Latte, (S)hot of Espresso:b
##TOTAL PRICE: $1.70
##=====================================================
##*                The Coffee Connection              *
##=====================================================
##Enter an option:
##C. Calculate price for coffee drink being ordered
##D. Display Coffee menu price information
##X. Exit
##ENTER YOUR MENU SELECTION:c
##ENTER THE COFFEE DRINK YOU WOULD LIKE TO ORDER: (B)lack Coffee, (C)appuccino, (L)atte, (M)ocha Latte, (S)hot of Espresso:l
##TOTAL PRICE: $3.20
##=====================================================
##*                The Coffee Connection              *
##=====================================================
##Enter an option:
##C. Calculate price for coffee drink being ordered
##D. Display Coffee menu price information
##X. Exit
##ENTER YOUR MENU SELECTION:x


