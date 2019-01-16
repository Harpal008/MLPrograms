# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:30:49 2019

@author: harpal
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('D:\Harpal\TechnicalStuff\Complete_ML_Own\Programs\ML_programs\dataset\Data.csv')
print(df.head())

plt.boxplot(df['Age'])
plt.show()
print(df['Age'].describe())
#box plot is used to find outliers

plt.hist(df['Age'])
plt.show()


plt.scatter(df['Age'],df['Salary'])
plt.show()

###Seaborn ####################
#u can add colors 
import seaborn as sns

#sea born style to your taste
sns.set_style("whitegrid")

df=pd.read_csv("D:\Harpal\TechnicalStuff\Complete_ML_Own\Programs\ML_programs\dataset\market_fact.csv")
print(df.head())

sns.distplot(df['Shipping_Cost'])
plt.show()

sns.distplot(df['Shipping_Cost'][:200],rug=True)
plt.show()

#rug tell where the desity is high or low


sns.distplot(df['Shipping_Cost'],hist=False)
plt.show()

plt.figure(1)
plt.subplot(2,2,1)
plt.title("Sales")
sns.distplot(df['Sales'])

plt.subplot(2,2,2)
plt.title("Profit")
sns.distplot(df['Profit'])

plt.figure(2)
plt.subplot(2,2,1)
plt.title("Order_Quantity")
sns.distplot(df['Order_Quantity'])



plt.subplot(2,2,2)
plt.title("Shipping Cost")
sns.distplot(df['Shipping_Cost'])
plt.show()

####BOX Plot ###############

sns.boxplot(df['Order_Quantity'])
plt.title("Order_Quantity")
plt.show()

##To make box plot on y axis

sns.boxplot(y=df['Order_Quantity'])
plt.title("Order_Quantity")
plt.show()

####   BiVariant Analysis ##############################
#We talk about two column

sns.jointplot('Sales','Profit',df)
plt.show()

#reomve point have extremly values
df=df[(df.Sales<20000) & (df.Profit<10000)]
sns.jointplot('Sales','Profit',df)
plt.show()

#Hex plot

df=df[(df.Profit<100) & (df.Profit>-100) &(df.Sales<200)]
#sns.jointplot('Sales','Profit',df,kind='hex',color="red")
sns.jointplot('Sales','Profit',df,kind='hex',color="red")
plt.show()























