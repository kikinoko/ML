import pandas as pd

# ファイルパスの指定
file_path = 'GOOG.csv'

# CSVファイルの読み込み
data = pd.read_csv(file_path)

# 日付列を日付型に変換
data['Date'] = pd.to_datetime(data['Date'])

# 日付順にデータを並べ替え
data = data.sort_values('Date')

# 前日比（DoD）を計算
data['DoD'] = data['Adj Close'].diff()

# Date, Adj Close, DoD列を表示
print(data[[ 'DoD']])
