# Sterling Kelly
# November 17 2025
# P3LAB
# This program asks the user for a money amount and calculates
# the most efficient number of dollars and coins.

# Ask the user for a money amount
amount = float(input("Enter the amount of money as a float: $"))

# Convert amount to cents
cents = int(amount * 100)

# Check if there is no money
if cents == 0:
    print("No change")

# Calculate dollars and coins if there is money
if cents != 0:
    dollars = cents // 100
    cents = cents - dollars * 100

    quarters = cents // 25
    cents = cents - quarters * 25

    dimes = cents // 10
    cents = cents - dimes * 10

    nickels = cents // 5
    cents = cents - nickels * 5

    pennies = cents

    # Print dollars
    if dollars == 1:
        print("1 Dollar")
    if dollars > 1:
        print(dollars, "Dollars")

    # Print quarters
    if quarters == 1:
        print("1 Quarter")
    if quarters > 1:
        print(quarters, "Quarters")

    # Print dimes
    if dimes == 1:
        print("1 Dime")
    if dimes > 1:
        print(dimes, "Dimes")

    # Print nickels
    if nickels == 1:
        print("1 Nickel")
    if nickels > 1:
        print(nickels, "Nickels")

    # Print pennies
    if pennies == 1:
        print("1 Penny")
    if pennies > 1:
        print(pennies, "Pennies")
