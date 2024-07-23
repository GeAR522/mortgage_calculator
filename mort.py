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
    monthly_payment = (
        principal
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** n_payments)
        / ((1 + monthly_interest_rate) ** n_payments - 1)
    )

    print("Your monthly payment is: ", monthly_payment)
    return [monthly_interest_rate, monthly_payment, n_payments]


def remaining_monthly_balance_plotter(params_list):
    [monthly_rate, monthly_payment, months] = params_list
    for i in range(months):
        # Calculate interest payment and add to list
        interest_payment = monthly_remaining_balance[i] * monthly_rate
        monthly_interest_payment.append(interest_payment)

        # Calculate capital payment and add to lis
        capital_payment = monthly_payment - interest_payment
        monthly_capital_payment.append(capital_payment)

        # Calculate remaining balance and add to list
        monthly_remaining_balance.append(monthly_remaining_balance[i] - capital_payment)

    for i in range(int(months / 12)):
        annual_remaining_balance.append(monthly_remaining_balance[i * 12])
        annual_capital_payments.append(
            sum(monthly_capital_payment[i * 12 : (i + 1) * 12])
        )
        annual_interst_payments.append(
            sum(monthly_interest_payment[i * 12 : (i + 1) * 12])
        )


mort_amount = input("Enter the value of your mortgage: ")
monthly_interest_rate = input("Enter your annual interest rate (Eg. 3.5% => 3.5): ")
years_left = input("Enter the number of years left on your mortgage: ")

balance_plotter_params = params_calculator(
    int(mort_amount), float(monthly_interest_rate), int(years_left)
)

remaining_monthly_balance_plotter(balance_plotter_params)

# print("capital")
# pp.pprint(monthly_capital_payment)
# print("interest")
# pp.pprint(monthly_interest_payment)
# print("remaining")
# pp.pprint(monthly_remaining_balance)
# print("annual remaining")
# pp.pprint(annual_remaining_balance)
# print("annual capital")
# pp.pprint(annual_capital_payments)
# print("annual interest")
# pp.pprint(annual_interst_payments)

monthly_pd = pd.DataFrame(
    [monthly_remaining_balance, monthly_capital_payment, monthly_interest_payment]
)
annual_pd = pd.DataFrame(
    [annual_remaining_balance, annual_capital_payments, annual_interst_payments]
)

pp.pprint(annual_pd)
pp.pprint(monthly_pd)
