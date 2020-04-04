#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 00:36:24 2019
132
@author: balderrama
"""
import pandas as pd
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score, cross_validate, cross_val_predict
from sklearn.model_selection import GridSearchCV
from sklearn.tree import export_graphviz
import matplotlib as mpl
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, Matern, ExpSineSquared, RationalQuadratic 
import numpy as np
from sklearn import linear_model
import time
from sklearn.model_selection import train_test_split
from joblib import dump
data = pd.read_excel('Data_Base.xls', index_col=0, Header=None)  
#data = data.loc[data['Renewable Capacity']>0]

'Renewable Invesment Cost'  'Battery Invesment Cost'

y = pd.DataFrame()
target= 'Invesment' #  
y[target] = data['Renewable Invesment Cost'] + data['Battery Invesment Cost'] + data['Generator Invesment Cost'] + 10000

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
#X['Generator Nominal capacity'] = data['Generator Nominal capacity'] 
X['HouseHolds'] = data['HouseHolds']
X['Renewable Energy Unit Total'] = data['Renewable Energy Unit Total']
#X['Max Demand'] = data['Max Demand']
#X['Y'] = data['Y']


feature_list = list(X.columns)
y, X = shuffle(y, X, random_state=10)

start = time.time()
l1 = [1,1,1,1,1,1,1,1,1,1]
l2 = [1,1,1,1,1,1,1,1,1,1]
#l3 = [1,1,1,1,1,1,1,1,1,1]

############################        NPC         ###############################    


#kernel =  (C()**2)*RBF(l1)
#kernel = Matern(l1)  +  Matern(l2) # +  Matern(l3)
kernel =  RBF(l1) + RBF(l2) #+ RBF(l3)
#kernel =  RBF(length_scale=l1,length_scale_bounds=(1e-5, 1e5)) #+ RBF(l2)


 
gp = GaussianProcessRegressor(kernel=kernel,n_restarts_optimizer=3000,
                              optimizer = 'fmin_l_bfgs_b'
#                              , normalize_y=True
                              
                              )

gp = gp.fit(X, y)

R_2_train = round(gp.score(X,y), 4)

print('R^2 for the gaussian process with the train data set is ' + str(R_2_train))

R_2_test = gp.score(X, y) 

print('R^2 for the gaussian process with the test data set is ' + str(R_2_test))

y_gp = gp.predict(X)
MAE_Random =  round(mean_absolute_error(y,y_gp),2)

print('MAE for the gaussian process is ' + str(MAE_Random))

end = time.time()
print('The Regression took ' + str(round(end - start,0)) + ' segundos')    

# gp.kernel_.get_params()
start = time.time()

filename = 'Invesment.joblib'
dump(gp, filename) 

