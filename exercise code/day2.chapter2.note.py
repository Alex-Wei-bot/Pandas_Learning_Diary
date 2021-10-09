import pandas as pd
from pandas.io.parsers import read_csv
# df_excel=pd.read_excel(r'D:\下载\my_excel.xlsx', parse_dates=['col5'])
# print(df_excel.tail())
# print(df_excel.shape)
# df_sep=pd.read_table('D:\下载\data\my_table_special_sep.txt',sep='\|\|\|\|',engine='python',header=None)
# print(df_sep.head())
# print(df_sep.shape)
df=read_csv('D:\下载\data\learn_pandas.csv',parse_dates=['Time_Record'])
print(df.columns)
print(df.head)
df=df[df.columns[:7]]
print(df.head)
print('\n')
print(df.describe)
print('\n')
print(df.info)