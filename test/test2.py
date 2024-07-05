from investment_calculator_package import *

swp = SWP_Calculator(
    initial_investment_amount = 16000000,
    rate_of_interest = 7,
    initial_monthly_withdrawal = 50000,
    inflation_rate = 7,
    number_of_years = 30
)

investment_df = swp.get_calculated_swp()
print(investment_df)