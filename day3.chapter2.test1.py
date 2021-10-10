import pandas as pd
from pandas.io.parsers import read_csv

df=read_csv('D:\下载\data\learn_pandas.csv',parse_dates=['Time_Record'])

dfdemo=df[['Weight','Height']]
s=pd.Series([1.235,2.788,2.0,6,7])
print(s.clip(1,3).replace({3:100}))