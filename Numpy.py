# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 07:37:52 2019

@author: harpal
"""

import numpy as np


a=np.array([1,2,3,4])
print(a )
print(type(a))

b=np.array([1,2,3,'test'])
print(b)
print(b.shape)
print(b.dtype)

c=np.array([[1,2,3,4],[11,22,33,44]])
print(c)
print(type(c))
print(c.shape) 
"""type of data does array contain"""
print(c.dtype) 
""" how many rows are present """
print(c.ndim)  

"""print values from 0 to 9"""
print(np.arange(10)) 

'''Below example shows hor fast numppy is '''
c=range(1000) #list
#%timeit [i**3 for i in c]
#o/p it took 4.35 ms+11us per loop

c_numpy=np.arange(1000)
#%timeit c_numpy**3
#o/p it took 27 us second

d=np.arange(10)
print(d)
e=np.arange(2,10)
print(e)
f=np.arange(2,10,2)
print(f)

g=np.zeros((3,2))
print(g)

g=np.ones((3,2))
print(g)

h=np.eye(3)
print(h)

h=np.eye(3,1)
print(h)

h=np.eye(3,2)
print(h)

i=np.full((3,2),2)
print(i)

i=np.full((3,2),2.2)
print(i)

i=np.full((3,2),2.2,dtype=np.int)
print(i)

j=np.diag([1,2,3,4,5])
print(j)

v=np.array([1,2,3])
print(np.tile(v,(3,1)))

a=np.random.random() #random values b/w 0-1
print(a)

b=50*np.random.random() +2
print(b)

c=np.random.random((3,2))
print(c)
print(c.dtype)

a=np.array([[1,2,3],[3,4,5]])
print(a)

b=np.array([[6,7,8],[9,10,11]])
print(b)
c=np.vstack((a,b))
print(c)

c=np.hstack((a,b))
print(c)

a=np.arange(10)
print(np.sign(a))
print(np.cos(a))
print(np.exp(a))

print(np.sum(a))

print(np.median(a))
print(np.std(a))

a=np.arange(1,10).reshape(3,3)
print(a)
print(np.linalg.det(a))
#print(np.linalg.inv(a))
print(np.linalg.eig(a))

b=np.arange(1,7).reshape(3,2)
print(a)
print(b)

print(np.dot(a,b))
a=np.array([1,1,0],dtype=bool)
b=np.array([1,0,1],dtype=bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))

print(a==a)
print(np.all(a==a))

a=np.array([[1,2],[3,4]])
print(a)
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

print(a.max())
print(a.argmax())

a=np.arange(10)
print(a.shape)

print(a[:,np.newaxis].shape)
print(np.sort(a))

a=np.array([1,2,3])
b=[11,12,13]
c=np.array(b)
print(a)
print(b)
print(c)

a=np.linspace(1,5,10)
print(a)
a=np.arange(1,10)
print(a)
a=np.arange(1,10,2)
print(a)




