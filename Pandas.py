# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:19:37 2019

@author: harpal
"""

"""Pandas 
used for Data Analysis,build on numpy
,Data Manupulation,Visualization,Building Ml Models

DataStructues in Pandas
1)Series
2)Dataframe
"""
#Series
print("####Series  #########")
import pandas as pd
a=pd.Series([1,2,3,4,5])
print(a)
print(type(a))

print(a[2])
print(a[2:])
print(a[2:5])
print(a)

a=pd.Series(['a','b','c'])
print(a)
print(type(a))
##In Pandas String is represted by Object ##


a=pd.date_range(start='01-01-2018',end='23-5-2018')
print(a)
print(type(a))

#DataFrame 
#Just like Tables
import numpy as np
print("****")
a=np.random.randint(low=20, high=100, size=[20,])
b=np.random.choice(['Ram','Tecclov','Ankit'],20)
c=np.random.choice([10,11,12,13],20)
c= np.arange(20)
print(a)
print(b)
print(c)
d=list(zip(a,b,c))
print(d)

#DataFrame
print("#########DataFrame###########")
df=pd.DataFrame(data=d,columns=['a','b','c'])
print(df)
print(type(df))

df=pd.DataFrame({'temp':a,'name':b,'random':c})
print(df)

print(df.shape)
print(df.columns)
print(df.name)
print(df['name'])
print(df['temp'].describe())
print(df.info())
print(df.values)
print(df)
print(df.set_index('temp',inplace=True))
print(df.sort_index(axis=0,ascending=False))
print(df.sort_values(by='random',ascending=False))
print(df.drop(['random'],axis=1))
print(df.head())

#Loc and Iloc
print("#########   iloc and loc ####################")
print(df.iloc[[0,1]])
print(df.iloc[1:3,1])
print(df.iloc[[True,True,False,True]]) #print rows only who are true 
print(df.head())
print(df.iloc[0,:])

print("###  LOC  ##############")
df=pd.DataFrame({'temp':a,'name':b,'random':c})      
print(df.set_index('random',inplace=True))
print(df.head())
print(df.loc[2,:])
print(df.loc[[1,2,4]])
print(df.loc[[1,2,4],'name':'temp'])
print(df.loc[[True,True,False,True]])
print(df.loc[df.temp>80])
print(df.loc[(df.temp>70)|(df.temp==80),:])

print("########Reading and Saving CSV ################")
df=pd.read_csv("D:\Harpal\TechnicalStuff\Complete_ML_Own\Programs\ML_programs\dataset\Data.csv")
print(df.head())
print(df.info())
#df.to_excel("df_excel.xlsx",sheet_name="Company_Data")  #saving to excel 
df2=pd.read_excel("df_excel.xlsx")
df2.to_csv("file.csv")  #Saving file to CSV
print(df2.head())
df2.to_csv("noindex.csv",index=False)

print("#######Merging data#######")
d1=pd.DataFrame([['a',1],['b',2]],columns=['col1','number'])
d2=pd.DataFrame([['c',3,'lion'],['b',4,'tiger']],columns=['letter','number','animal'])
print(d1)
print(d2)

print(pd.concat([d1,d2],axis=0)) 
#for new index
print(pd.concat([d1,d2],axis=0,ignore_index=True))
print("#############################################")
print(pd.concat([d1,d2],axis=1))
print(df.shape)
print(df.columns)
print(df.Age)
print(df[['Age','Salary']])
print(df['Age'].describe())
print(df.info())
print(df.values) #return an array
print(df)






 



