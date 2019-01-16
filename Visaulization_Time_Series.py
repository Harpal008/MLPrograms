# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 09:17:09 2019

@author: harpal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

market_df=pd.read_csv('D:\Harpal\TechnicalStuff\Complete_ML_Own\Programs\ML_programs\dataset\market_fact.csv')
customer_df=pd.read_csv('D:\Harpal\TechnicalStuff\Complete_ML_Own\Programs\ML_programs\dataset\cust_dimen.csv')
product_df=pd.read_csv('D:\Harpal\TechnicalStuff\Complete_ML_Own\Programs\ML_programs\dataset\prod_dimen.csv')
shipping_df=pd.read_csv('D:\Harpal\TechnicalStuff\Complete_ML_Own\Programs\ML_programs\dataset\shipping_dimen.csv')
orders_df=pd.read_csv('D:\Harpal\TechnicalStuff\Complete_ML_Own\Programs\ML_programs\dataset\orders_dimen.csv')

print(market_df.head())

#Merging the data
print("###########Merging Data ###############")
df=pd.merge(market_df,orders_df,how='inner',on='Ord_id')
print(df.head())
print(df.info())

#Conver order_date columns from object to date
df['Order_Date']=pd.to_datetime(df['Order_Date'])
print(df.info())

time_df=df.groupby('Order_Date')['Sales'].sum()
print(time_df.head())
print(type(time_df))

#Timeplot 
plt.figure(figsize=(16,8))
sns.tsplot(data=time_df)
plt.show()

#featch out mont and year
df['month']=df['Order_Date'].dt.month
df['year']=df['Order_Date'].dt.year

print(df.head())

#mean values of year and month
df_time=df.groupby(['year','month']).Sales.mean()
print(df_time.head())


plt.figure(figsize=(8,6))
#time series plot
sns.tsplot(df_time)
plt.xlabel("Time")
plt.ylabel("Sales")
plt.show()

#Creating pivot table
print("#### Pivot Table##############")
year_month=pd.pivot_table(df,values='Sales',index='year',columns='month',aggfunc='mean')
print(year_month.head())
 
plt.figure(figsize=(12,8))
sns.heatmap(year_month,cmap="YlGnBu")
plt.show()







