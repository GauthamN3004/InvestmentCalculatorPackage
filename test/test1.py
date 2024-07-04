from investment_calculator_package import *
sip = SIP_Calculator()
location = 'D:/Documents/Code/Github/InvestmentCalculatorPackage/test/sip_sample.csv'
sip.add_investments(csv_location = location)
print(sip.investment_dataframe)
