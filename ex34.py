import pandas as pd
import matplotlib.pyplot as plt


file_path = 'GOOG.csv'  
data = pd.read_csv(file_path)

# 日付の列をdatetime型に変換
data['Date'] = pd.to_datetime(data['Date'])

# 時系列順にデータを並び替え
data_sorted = data.sort_values('Date')

# "Adj Close"列をプロット
plt.plot(data_sorted['Date'], data_sorted['Adj Close'], label="Adj Close")

plt.grid(True)
plt.show()
