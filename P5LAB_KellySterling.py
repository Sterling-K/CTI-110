#Sterling Kelly
#December 12, 2025
#P5LAB
#Simulates a self checkout machine and disperses change

import random

def disperse_change(change):
    cents = int(round(change * 100))

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    if dollars > 0:
        print(f"{dollars} Dollars")
    if quarters > 0:
        print(f"{quarters} Quarters")
    if dimes > 0:
        print(f"{dimes} Dimes")
    if nickels > 0:
        print(f"{nickels} Nickels")
    if pennies > 0:
        print(f"{pennies} Pennies")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")

    cash = float(input("How much cash will you put in the self-checkout?\n"))

    change = round(cash - amount_owed, 2)
    print(f"Change is: ${change}")

    disperse_change(change)

main()
