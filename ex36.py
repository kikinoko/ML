import pandas as pd


file_path = 'GOOG.csv' 
data = pd.read_csv(file_path)

data['Date'] = pd.to_datetime(data['Date'])

data = data.sort_values('Date')

#diff()は、直前の行との差分を計算
data['DoD'] = data['Adj Close'].diff()

print(data[['Date', 'Adj Close', 'DoD']])
