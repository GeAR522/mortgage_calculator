import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pprint as pp

annual_remaining_balance = []
annual_capital_payments = []
annual_interst_payments = []

monthly_remaining_balance = []
monthly_interest_payment = []
monthly_capital_payment = []


def params_calculator(principal, annual_interest_rate, years):
    # Add initial total to index 0 of remaining balance
    monthly_remaining_balance.append(principal)

    # Convert annual interest rate to monthly and percentage to decimal
    monthly_interest_rate = annual_interest_rate / 12 / 100
    # Total number of monthly payments
    n_payments = years * 12

    # Calculate monthly payment using the formula
    monthly_payment = round((
        principal
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** n_payments)
        / ((1 + monthly_interest_rate) ** n_payments - 1)
    ), 2)

    print("Your monthly payment is: ", monthly_payment)
    return [monthly_interest_rate, monthly_payment, n_payments]


def remaining_monthly_balance_plotter(params_list):
    [monthly_rate, monthly_payment, months] = params_list
    for i in range(months):
        # Calculate interest payment and add to list
        interest_payment = round(monthly_remaining_balance[i] * monthly_rate, 2)
        monthly_interest_payment.append(interest_payment)

        # Calculate capital payment and add to lis
        if monthly_payment >= monthly_remaining_balance[i]:
            monthly_capital_payment.append(monthly_remaining_balance[i])
        else:
            capital_payment = round(monthly_payment - interest_payment, 2)
            monthly_capital_payment.append(capital_payment)

        # As we have an entry 0 being the intial, we are already +1 compared to the above lists, so this remaining balance isn't needed for the last entry.
        if i < months - 1:
            # Calculate remaining balance and add to list
            monthly_remaining_balance.append(round(monthly_remaining_balance[i] - capital_payment, 2))

    years = int(months / 12)
    for i in range(years):
        annual_remaining_balance.append(monthly_remaining_balance[i * 12])
        
        annual_capital_payments.append(
            round(sum(monthly_capital_payment[i * 12 : (i + 1) * 12])
        , 2))
        annual_interst_payments.append(
           round(sum(monthly_interest_payment[i * 12 : (i + 1) * 12])
        , 2))

def main():
    while True:
        print("\n Calculate mortgage payments?")

        choice = input("Y/N: ").upper()
        if choice == "Y":
            annual_remaining_balance.clear()
            annual_capital_payments.clear()
            annual_interst_payments.clear()

            monthly_remaining_balance.clear()
            monthly_interest_payment.clear()
            monthly_capital_payment.clear()

            mort_amount = input("Enter the value of your mortgage: ")
            monthly_interest_rate = input("Enter your annual interest rate (Eg. 3.  5% => 3.5): ")
            years_left = input("Enter the number of years left on your mortgage: ")

            balance_plotter_params = params_calculator(
            int(mort_amount), float(monthly_interest_rate), int(years_left)
            )

            remaining_monthly_balance_plotter(balance_plotter_params)

            monthly_pd = pd.DataFrame(
            [monthly_remaining_balance, monthly_capital_payment,    monthly_interest_payment]
            )
            annual_pd = pd.DataFrame(
                [annual_remaining_balance, annual_capital_payments,     annual_interst_payments]
            )
            pp.pprint(annual_pd)
            pp.pprint(monthly_pd)

            create_workbook = input("Would you like to create an excel workbook of these results? (Y): ").upper()

            if create_workbook == "Y":
                print("Creating workbook...")

                with pd.ExcelWriter("mortgage_results.xlsx") as writer:
                    monthly_pd.to_excel(writer, sheet_name="Monthly")
                    annual_pd.to_excel(writer, sheet_name="Annual")    
            else:
                break


        elif choice == "N":
            print("bye")
            break
        else:
            print("Invalid choice. Please try again.")

main()
