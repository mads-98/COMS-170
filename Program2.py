# Madison Cronk
# 0582982
# Program #2
# COMS-170-01: Winter 2025
# Due: 01-30-2025
# Program #2 - Calculate final price of a new computer using employee discount. 
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# fltDiscount           float       stores value representing the discount percentage
# fltTax                float       stores value of tax percentage to be charged
# fltOPrice             float       stores original price
# fltDPrice             float       stores value of discounted price
# fltTaxA               float       stores value of tax amount based off of tax percentage
# fltFPrice             float       stores the value of the final price after calculating the discount price and cost of tax

# Create variables and assign values
fltDiscount = 0.12
fltTax = 0.07
fltOPrice = float(input('Enter original price:'))

# Perform calculations and operations
fltDPrice = fltOPrice-fltDiscount*fltOPrice
fltTaxA = fltDPrice*fltTax
fltFPrice = fltTaxA+fltDPrice

# Display output to user
print(f'The original price entered was {fltOPrice:.2f}')
print(f'The discounted price before tax is {fltDPrice:.2f}')
print(f'The amount of tax to be paid on this product is {fltTaxA:.2f}')
print(f'After calculating the discount and sales tax the final price would be {fltFPrice:.2f}')

# Add Output of final program as Comments
##=================== RESTART: /Users/mads/Desktop/Program2.py ===================
##Enter original price:599.99
##The original price entered was 599.99
##The discounted price before tax is 527.99
##The amount of tax to be paid on this product is 36.96
##After calculating the discount and sales tax the final price would be 564.95
