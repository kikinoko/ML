import pandas as pd
from datetime import datetime, timedelta


file_path = 'GOOG.csv'  
data = pd.read_csv(file_path)

# 日付の列をdatetime型に変換
data['Date'] = pd.to_datetime(data['Date'])

current = datetime.now()
one_month_ago = current - timedelta(days=31)

# 最近1ヶ月のデータに絞る
recent = data[data['Date'] >= one_month_ago]
print(recent)
