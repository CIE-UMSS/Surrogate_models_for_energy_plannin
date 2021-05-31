# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:40:45 2021

@author: Dell
"""


import pandas as pd

Village_Population = list(range(50,570,50))

Demand = pd.DataFrame()
Demand_Average = pd.DataFrame()

for i in Village_Population:
    
    sheet_name = 'village_' + str(i)
    
    Energy_Demand = pd.read_excel('Demand_Expected.xls',sheet_name=sheet_name
                                  ,index_col=0,Header=None)
        
    Energy_Demand_Non_Cooking = pd.read_excel('Demand_Expected_Non_Cooking.xls', 
                                                  sheet_name=sheet_name, index_col=0,
                                                   Header=None)
        
    Demand[sheet_name + '_' + 'Cooking'] = Energy_Demand[1]
    Demand[sheet_name + '_' + 'Non_Cooking'] = Energy_Demand_Non_Cooking[1]
    Demand['Dif_'+sheet_name] = Energy_Demand[1] -  Energy_Demand_Non_Cooking[1]
    
    Demand_Average.loc[sheet_name,'Average'] = Demand[sheet_name + '_' + 'Non_Cooking'].sum()/Demand[sheet_name + '_' + 'Cooking'].sum()
    