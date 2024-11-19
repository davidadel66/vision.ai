import requests
import pandas as pd
from config import ALPHA_VANTAGE_API_KEY

class stockUniverse:
    def __init__(self, symbol):
        self.ticker = symbol
        self.api_key = ALPHA_VANTAGE_API_KEY
        self.historical_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.ticker}&outputsize=full&apikey={self.api_key}"
        self.earnings_url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={self.ticker}&apikey={self.api_key}"
        self.fundamentals_url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={self.ticker}&apikey={self.api_key}"
    
    def get_daily_data(self):
        response = requests.get(self.historical_url)
        data = response.json()
        print(data)
        df = pd.DataFrame(data["Time Series (Daily)"]).T
        df.rename(columns={'1. open': 'open', 
                           '2. high': 'high', 
                           '3. low': 'low', 
                           '4. close': 'close', 
                           '5. volume': 'volume'}, inplace=True)
        return df
    
    def get_returns(self):
        df = self.get_daily_data()
        returns = df['close'].pct_change()
        return returns
    
    def get_earnings_reports(self):
        response = requests.get(self.earnings_url)
        data = response.json()
        earnings = {}
        for quarter in data['quarterlyReports']:
            for key, value in quarter.items():
                if key not in earnings:
                    earnings[key] = []
                earnings[key].append(value)
            
        earnings_df = pd.DataFrame(earnings)
        return earnings_df
    
    def get_fundamentals(self):
        response = requests.get(self.fundamentals_url)
        data = response.json()
        print(data)

    def get_balance_sheet(self):
        url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=AAPL&apikey={self.api_key}'
        r = requests.get(url)
        data = r.json()
        print(data) 