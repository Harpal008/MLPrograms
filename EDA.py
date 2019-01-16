# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:04:55 2019

@author: harpal
"""
'''
5 Steps for EDA
1)Sourcing
2)Cleaning(most imp,find out any missing value)
3)Univariant Analysis(try out pattern)
4)Bivariate(Pair of columns)
5)Derived Metrics (get new columns out of existing columns)


Sourcing 
a)Public Data
b)Private Data

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast,json

from datetime import datetime


credits_df=pd.read_csv('D:/Harpal/TechnicalStuff/Complete_ML_Own/Programs/ML_programs/dataset/tmdb_5000_credits.csv')
movies_df=pd.read_csv('D:/Harpal/TechnicalStuff/Complete_ML_Own/Programs/ML_programs/dataset/tmdb_5000_movies.csv')

print(movies_df.head())


