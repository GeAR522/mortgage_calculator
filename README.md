# Mortgage Calculator

This is just a simple python programme which will calculate the monthly payment of a mortgage based on the total value of the mortgage, the rate of the mortgage, and the remaining number of years.

From this you will be told the monthly payment and displayed a breakdown of the monthly payments for the duration of the mortgage including: 
the remaining balance for each month, the capital payment of each month, and the interest payment of each month.

As I do not ask what the startdate of the mortgage is, this uses an averaged rate of 365/12 = 30.42 for each month rather than the precise number of days per month. It's not explicitly written, but is inferred via taking the annual rate and dividing by 12 to get the monthly rate as if each month were 30.42 days.

You will also see the annual breakdown of the mortgage including:
the remaining balance of each year, the capital payments for each year, and the interest payments of each year.

Afterwards you will be asked if you would like these to be exported to a locally saved xlsx file which will be called 'mortgage_results'.
The first Sheet will be the monthly results, the second sheet will be the annual results.

If you rerun the programme it will overwrite the existing xlsx file.

This is something I use regularly and it helps me keep track of the costs for potential changes in mortgage down the line.
