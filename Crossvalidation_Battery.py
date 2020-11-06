#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:03:33 2019

@author: balderrama
"""

import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import cross_val_score, cross_validate, cross_val_predict
import matplotlib as mpl
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, WhiteKernel
import numpy as np
from sklearn import linear_model
from math import sqrt as sq
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
#%%
# Data manipulation
data = pd.read_excel('Databases/Data_Base.xls', index_col=0, Header=None)  

#%%
y = pd.DataFrame()
target= 'Battery Capacity'
y[target] = data[target]

y=y.astype('float')

X = pd.DataFrame()
X['Renewable Invesment Cost'] = data['Renewable Unitary Invesment Cost']   
X['Battery Unitary Invesment Cost'] = data['Battery Unitary Invesment Cost']
X['Deep of Discharge'] = data['Deep of Discharge']
X['Battery Cycles'] = data['Battery Cycles']
X['GenSet Unitary Invesment Cost'] = data['GenSet Unitary Invesment Cost']
X['Generator Efficiency'] = data['Generator Efficiency']
X['Low Heating Value'] = data['Low Heating Value']
X['Fuel Cost'] = data['Fuel Cost']
X['HouseHolds'] = data['HouseHolds']
X['Renewable Energy Unit Total'] = data['Renewable Energy Unit Total']



feature_list = list(X.columns)
y, X = shuffle(y, X, random_state=10)

#%%
# Linear regression
# Linear Cross validation

scoring =   ['r2', 'neg_mean_absolute_error', 'neg_mean_squared_error'] #'r2' 'neg_mean_absolute_error' # 'neg_mean_squared_error'
for i in scoring:
    
    lm = linear_model.LinearRegression(fit_intercept=False)
    scores = cross_val_score(lm, X, y, cv=5,scoring=i)
    score = round(scores.mean(),2)
    
    if i == 'neg_mean_squared_error':
        score = sq(-score)    
        print(i + ' for the gaussian process with the test data set is ' + str(score))
    else:    
        print(i + ' for the gaussian process with the test data set is ' + str(score))


#%%
# Cross Validation results
scoring =   ['r2', 'neg_mean_absolute_error', 'neg_mean_squared_error'] 
for i in scoring:        
        
    l1 = [1,1,1,1,1,1,1,1,1,1]
    l2 = [1,1,1,1,1,1,1,1,1,1]
    

    kernel = RBF(l1) + RBF(l2) # + RBF(l3)
    gp = GaussianProcessRegressor(kernel=kernel,optimizer = 'fmin_l_bfgs_b', 
                                  n_restarts_optimizer=3000)
    
    Results = cross_validate(gp, X, y, cv=5,return_train_score=True,n_jobs=-1
                             , scoring = i       )
    
    scores = Results['test_score']
    score = round(scores.mean(),2)
    
    if i == 'neg_mean_squared_error':
        score = sq(-score)    
        print(i + ' for the gaussian process with the test data set is ' + str(score))
    else:    
        print(i + ' for the gaussian process with the test data set is ' + str(score))
    Results = pd.DataFrame(Results)
    
    path = 'Results_Regressions/Kcross_valiadation_GP_Bat' + '_' +  i + '.csv'
    Results.to_csv(path)



