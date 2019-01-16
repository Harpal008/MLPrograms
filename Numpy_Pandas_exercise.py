# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 08:06:14 2019

@author: harpal
"""
import numpy as np
import pandas as pd

d=np.array([1,2,3,4,5,6])
print(d)

d=np.arange(10)
print(d)

d=np.linspace(1,3,6)
print(d)

c=[11,22,33,44,55,66]
d=np.array(c)
print(d)

d=pd.Series([1,2,3,45])
print(d)
print(type(d))
print(d.shape)

c=[]
for x in d:
    c.append(x)
print(c)
print(type(c))

c=d.tolist()
print(c)
print(type(c))

a=pd.Series([2,4,6,8,10])
b=pd.Series([1,4,5,7,9])

print(a)
print(b)

print("#############################################")
print(a[:]+b[:])
print(a[:]-b[:])
print(a[:]/b[:])

print(a+b)
print(a-b)
print(a/b)

print(a.max())
print(b.max())

print(a.min())

print(a==b)
print(a<b)
print(a>b)

##Write a Python program to convert a dictionary to a Pandas series
b={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
z=pd.Series(b)
print(z)

##Write a Python program to convert a NumPy array to a Pandas series. 
a=np.array([10, 20, 30, 40, 50])
b=pd.Series(a)
print(b)

###Write a Python program to change the data type of given a column or a Series
a=np.array([10, 20,'Python', 40, 50])
b=pd.Series(a,dtype=object)
print(b)
c=pd.to_numeric(b,errors='coerce')
print(c)

##Write a Python Pandas program to convert the first column of a DataFrame as a Series.
a=np.array([1,2,3])
b=np.array([5,6,7])
c=np.array([5,8,12])

z=pd.DataFrame(data=[a,b,c])
print(z)

x=pd.Series(z[0])
print(x)
print(type(x))

# Write a Pandas program to convert a given Series to an array
x=pd.Series(z[0])
print(x)
print(type(x))
aa=np.array(x)
print(aa)
print(type(aa))

bb = np.array(x.values.tolist())
print(bb)
print(type(bb))

##Write a Pandas program to convert Series of lists to one Series
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print("Original Series of list")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)

##Write a Pandas program to sort a given Series
a=pd.Series(['100','200','python','300.12','400'])
print(a)
print(a.sort_values())
#print(pd.Series(a).sort_values())
a_new=a.append(pd.Series([1111,22222]))
print(a_new)

#Write a Pandas program to create a subset of a given series based on value and condition
a=np.arange(11)
b=pd.Series(a)
print(b)
print(b[b[:]<6])
print(b[b<6])

#Write a Pandas program to change the order of index of a given 
a=pd.Series([1,2,3,4,5,],index=['A','B','C','D','E'])
print(a)
b=a.reindex(['B','A','C','D','E'])
print(b)

print(a.mean())
print(a.std())

#Write a Pandas program to get the powers of an array values element-wise
data= {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
a=pd.DataFrame(data)
print(a)

#Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
a=pd.DataFrame(exam_data,index=labels)
print(a)

#Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

a=pd.DataFrame(exam_data,index=labels)
print(a)
print(a.info())

# Write a Pandas program to get the first 3 rows of a given DataFrame
print(a[:3])

#Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame
print("###########################################################################")
print(a[['name','score']])

#Write a Pandas program to select the specified columns and rows from a given data frame
print(a[['name','score']])

print(a.iloc[[1, 3, 5, 6], [1, 3]])

#Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2
print(a[a['attempts']>2])
#print(a.ix[[1, 3, 5], ['name', 'score']])

#Write a Pandas program to count the number of rows and columns of a DataFrame
print(a)
print(a.shape)
print(len(a.axes[0]))
print(len(a.axes[1]))

#Write a Pandas program to select the rows where the score is missing
print(a[a['score'].isnull()])

#Write a Pandas program to select the rows the score is between 15 and 20 (inclusive)
print(a[a['score'].between(15,20)])

# Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15
print()






















