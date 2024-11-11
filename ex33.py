import pandas as pd

# CSVファイルの読み込み
file_path = 'GOOG.csv'  
data = pd.read_csv(file_path)

# 列名をリストで取得
column_names = data.columns.tolist()

# 列名を標準出力
print(column_names)
