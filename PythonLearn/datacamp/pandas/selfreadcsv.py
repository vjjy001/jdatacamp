import pandas as pd

df1 = pd.read_csv('messy_stock_data.tsv',delimiter=' ',header=3,comment='#')

print(df1.head())
