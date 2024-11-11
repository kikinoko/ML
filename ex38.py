import pandas as pd

file_path = 'sample.csv'
df = pd.read_csv(file_path)


num = df.select_dtypes(include='number') 
df[num.columns] = num.fillna(num.mean())  #.colums->dfの列名取得

print(df)
