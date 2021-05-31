# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:31:30 2021

@author: Dell
"""


import pandas as pd

Village_Population = list(range(50,570,50))
energy = pd.DataFrame()

for i in Village_Population:
    
    sheet_name = 'village_' + str(i)
    
    Energy_Demand_Paper = pd.read_excel('Demand_Paper.xls',sheet_name=sheet_name
                                  ,index_col=0,Header=None)
        
    Energy_Demand_Non_Cooking = pd.read_excel('Demand_Expected_Non_Cooking.xls', 
                                                  sheet_name=sheet_name, index_col=0,
                                                   Header=None)
    
    print(i)
    print( round(Energy_Demand_Paper[1].sum(),5) == round(Energy_Demand_Non_Cooking[1].sum(),5))
    
    energy.loc[i,'Total Demand'] =  round(Energy_Demand_Non_Cooking[1].sum(),5)/1000