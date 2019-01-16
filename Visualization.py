# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:49:44 2019

@author: harpal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#plotiing two 1-d Array
x=np.linspace(5,100,10)
y=np.linspace(5,1000,10)

print(x)
print(y)

plt.plot(x,y)

#plt.plot([1,4,6,8],[3,8,3,5])

plt.xlabel("Current")
plt.ylabel("Voltage")
plt.title("Ohm's Law")
plt.xlim([20,80])
plt.ylim([200,800])
plt.show()

y=x*2
plt.plot(x,y,'b+')
plt.plot(x,y,'r-',x,y**2,'b+',x,y**3,'g^')
plt.show()

#Figures and Subplots
x=np.linspace(1,10,100)
y=np.log(x)

plt.figure(1)
#create first subplot
plt.subplot(121)
plt.title("y=log(x)")
plt.plot(x,y)

#create Second subplot
plt.subplot(122)
plt.title("y=log(x)**2")
plt.plot(x,y**2)

plt.show()

#################################################
#Create 4 subplot
'''plt.figure(1)


plt.subplot(1,4,1)
plt.title("Square")
plt.plot(x,y**2)

plt.subplot(1,4,2)
plt.title("Cube")
plt.plot(x,y**3)

plt.subplot(1,4,3)
plt.title("linear")
plt.plot(x,y)

plt.subplot(1,4,4)
plt.title("Root")
plt.plot(x,y*0.2)
plt.show()
'''
#######################################################
'''
plt.figure(1)
plt.subplot(2,2,1)
plt.title("Square")
plt.plot(x,y**2)

plt.subplot(2,2,2)
plt.title("Cube")
plt.plot(x,y*3)

plt.Figure(2)
plt.subplot(2,2,1)
plt.title("linear")
plt.plot(x,y)

plt.subplot(2,2,2)
plt.title("Root")
plt.plot(x,y*0.2)
plt.show()
'''
#######################################################

#
#plt.subplot(nrows,ncols,nsubplot)

'''
plt.figure(1)
plt.subplot(3,3,1)
plt.title("Square")
plt.plot(x,y**2)


plt.subplot(3,3,2)
plt.title("Cube")
plt.plot(x,y**3)

plt.subplot(3,3,3)
plt.title("line")
plt.plot(x,y)


plt.Figure(2)
plt.subplot(3,3,1)
plt.title("linear")
plt.plot(x,y)

plt.subplot(3,3,2)
plt.title("Root")
plt.plot(x,y*0.2)

plt.subplot(3,3,3)
plt.title("line")
plt.plot(x,y)


plt.Figure(3)
plt.subplot(3,3,1)
plt.title("linear")
plt.plot(x,y)

plt.subplot(3,3,2)
plt.title("Root")
plt.plot(x,y*0.2)

plt.subplot(3,3,3)
plt.title("line")
plt.plot(x,y)

plt.show()
'''
############################################################








