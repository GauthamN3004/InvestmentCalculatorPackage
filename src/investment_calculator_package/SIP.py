import pandas as pd

class SIP_Calculator():
    def __init__(self):
        self.investment_dataframe = None

    def validate_dataframe(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise("Not a pandas dataframe.")
        
        df_columns = dataframe.columns
        required_columns = ['amount', 'rate_of_interest', 'number_of_years']
        
        if len(df_columns) != 3:
            raise("The dataframe should contain 3 columns (amount, rate_of_interest, number_of_years) - found {0}".format(len(df_columns)))

        for column in required_columns:
            if column not in df_columns:
                raise("The dataframe is missing '{0}' column. Following columns were found - {1}".format(column, str(list(df_columns))))

        # check if all values are numeric
        try:
            pd.to_numeric(dataframe['amount'])
            pd.to_numeric(dataframe['rate_of_interest'])
            pd.to_numeric(dataframe['number_of_years'])
        except:
            raise("The values are not numeric.")

        return

        
    def add_investments(self, csv_location, is_header_present = True):
        header = None
        if is_header_present:
            header = 0

        dataframe = pd.read_csv(csv_location, header = header)
        self.validate_dataframe(dataframe)
        self.investment_dataframe = dataframe
        return