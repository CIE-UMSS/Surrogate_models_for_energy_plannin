#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:16:49 2019

@author: balderrama
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
#%%
# Data load
data = pd.read_excel('Databases/Database.xls', index_col=0, Header=None)   

#%%

time = round(data['Time'].sum()/3600,0)
time_average = round(data['Time'].mean(),0)
gap = round(data['Gap'].mean(),1)
print('The database creation process took ' + str(time) + ' hours')
print('The average resolution time was ' + str(time_average) + ' seconds')
print('The average gap is ' + str(gap) + ' %')


#%%
# Data results

mean = data.mean()
Datos = pd.DataFrame()

Datos.loc['NPC (thousands USD)', 'Mean'] = mean['NPC'] 
Datos.loc['LCOE (USD/kWh)', 'Mean'] = mean['LCOE'] 
Datos.loc['PV nominal capacity (kW)', 'Mean'] = mean['Renewable Capacity'] 
Datos.loc['Battery nominal capacity (kWh)', 'Mean'] = mean['Battery Capacity'] 
Datos.loc['Renewable energy penetration (%)', 'Mean'] = mean['Renewable Penetration']*100 
Datos.loc['Battery usage (%)', 'Mean'] = mean['Battery Usage Percentage'] 
Datos.loc['Energy curtail (%)', 'Mean'] = mean['Curtailment Percentage'] 

Max = data.max()

Datos.loc['NPC (thousands USD)', 'Max'] = Max['NPC'] 
Datos.loc['LCOE (USD/kWh)', 'Max'] = Max['LCOE'] 
Datos.loc['PV nominal capacity (kW)', 'Max'] = Max['Renewable Capacity'] 
Datos.loc['Battery nominal capacity (kWh)', 'Max'] = Max['Battery Capacity'] 
Datos.loc['Renewable energy penetration (%)', 'Max'] = Max['Renewable Penetration']*100 
Datos.loc['Battery usage (%)', 'Max'] = Max['Battery Usage Percentage'] 
Datos.loc['Energy curtail (%)', 'Max'] = Max['Curtailment Percentage'] 

Min = data.min()

Datos.loc['NPC (thousands USD)', 'Min'] = Min['NPC'] 
Datos.loc['LCOE (USD/kWh)', 'Min'] = Min['LCOE'] 
Datos.loc['PV nominal capacity (kW)', 'Min'] = Min['Renewable Capacity'] 
Datos.loc['Battery nominal capacity (kWh)', 'Min'] = Min['Battery Capacity'] 
Datos.loc['Renewable energy penetration (%)', 'Min'] = Min['Renewable Penetration']*100 
Datos.loc['Battery usage (%)', 'Min'] = Min['Battery Usage Percentage'] 
Datos.loc['Energy curtail (%)', 'Min'] = Min['Curtailment Percentage'] 


std = data.std()

Datos.loc['NPC (thousands USD)', 'Std'] = std['NPC'] 
Datos.loc['LCOE (USD/kWh)', 'Std'] = std['LCOE'] 
Datos.loc['PV nominal capacity (kW)', 'Std'] = std['Renewable Capacity'] 
Datos.loc['Battery nominal capacity (kWh)', 'Std'] = std['Battery Capacity'] 
Datos.loc['Renewable energy penetration (%)', 'Std'] = std['Renewable Penetration']*100 
Datos.loc['Battery usage (%)', 'Std'] = std['Battery Usage Percentage'] 
Datos.loc['Energy curtail (%)', 'Std'] = std['Curtailment Percentage'] 

Datos.to_latex('table')


#%%


data_1 = MinMaxScaler().fit_transform(data)
data_1 = pd.DataFrame(data_1, columns=data.columns)

data_2 = pd.DataFrame()
for i in data.columns:
    foo = data_1[i]
    foo = foo.sort_values( ascending=False)
    data_2[i] = foo.values
    
index_LDC = []
for i in range(len(data_2)):
    index_LDC.append((i+1)/float(len(data_2))*100)
    
data_2.index = index_LDC    


size = [20,15]
label_size = 25
tick_size = 25 

fig=plt.figure(figsize=size)
ax=fig.add_subplot(111, label="1")
mpl.rcParams['xtick.labelsize'] = tick_size 
mpl.rcParams['ytick.labelsize'] = tick_size 

#ax.plot(index_LDC, data_2['NPC'], c='b')
#ax.plot(index_LDC, data_2['LCOE'], c='k')
ax.plot(index_LDC, data_2['Renewable Capacity'], c='y')
ax.plot(index_LDC, data_2['Battery Capacity'], c='g')
ax.plot(index_LDC, data_2['Renewable Penetration'], c='r')
ax.plot(index_LDC, data_2['Battery Usage Percentage'], c='c')
ax.plot(index_LDC, data_2['Curtailment Percentage'], c='m')

# limits
ax.set_xlim([0,100])
ax.set_ylim([0,1])
# labels
ax.set_xlabel('%',size=label_size) 
#ax.set_ylabel('HouseHolds',size=label_size) 
#NPC = mlines.Line2D([], [], color='b',label='NPC')
#LCOE = mlines.Line2D([], [], color='k',label='LCOE')
Battery_Capacity = mlines.Line2D([], [], color='g',label='Battery nominal capacity')
PV_Capacity = mlines.Line2D([], [], color='y',label='PV nominal capacity')
Renewable_Penetration = mlines.Line2D([], [], color='r',label='Renewable energy penetration')
Battery_Usage = mlines.Line2D([], [], color='c',label='Battery usage')
Energy_Curtailment = mlines.Line2D([], [], color='m',label='Energy curtail')

plt.legend(handles=[
#        NPC, 
#        LCOE, 
        PV_Capacity,
        Battery_Capacity, 
        Renewable_Penetration,
                   Battery_Usage, Energy_Curtailment
 ], bbox_to_anchor=(1, 1),fontsize = 20)

plt.savefig('Plots/Duration_Curve_Results.png', bbox_inches='tight')    
plt.show()   

#%%
# duration curve of NPC and LCOE
data_3 = pd.DataFrame()
for i in ['NPC', 'LCOE']:
    foo = data[i]
    foo = foo.sort_values( ascending=False)
    data_3[i] = foo.values

index_LDC = []
for i in range(len(data_3)):
    index_LDC.append((i+1)/float(len(data_3))*100)
    
data_3.index = index_LDC    


size = [20,15]
label_size = 25
tick_size = 25 

fig=plt.figure(figsize=size)
ax=fig.add_subplot(111, label="1")
ax2=fig.add_subplot(111, label="2", frame_on=False)

mpl.rcParams['xtick.labelsize'] = tick_size 
mpl.rcParams['ytick.labelsize'] = tick_size 

ax.plot(index_LDC, data_3['NPC']/1000, c='b')
ax2.plot(index_LDC, data_3['LCOE'], c='k')

ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right') 
# limits
ax.set_xlim([0,100])
ax.set_ylim([0,1500])
ax2.set_xlim([0,100])
ax2.set_ylim([0,0.8])
# labels
ax.set_xlabel('%',size=label_size) 
ax.set_ylabel('NPC (Thousand USD)',size=label_size) 
ax2.set_ylabel('LCOE (kWh/USD)',size=label_size) 

NPC = mlines.Line2D([], [], color='b',label='NPC')
LCOE = mlines.Line2D([], [], color='k',label='LCOE')


plt.legend(handles=[ NPC, LCOE ], bbox_to_anchor=(1, 1),fontsize = 20)

plt.savefig('Plots/Duration_Curve_Costos.png', bbox_inches='tight')    
plt.show()   

#%%
# Box plots NPC and LCOE
BoxPlot_NPC  = []
BoxPlot_LCOE = []

for i in range(50,570,50):
    df = data.loc[data['HouseHolds']==i]
    df.index = range(150)
    BoxPlot_NPC.append(df['NPC']/1000)
    BoxPlot_LCOE.append(df['LCOE'])
        
tick_size = 25 
label_size = 25
title_size = 50
fig, axs = plt.subplots(2, figsize=(20, 15))
mpl.rcParams['xtick.labelsize'] = tick_size 
mpl.rcParams['ytick.labelsize'] = tick_size 

axs[0].boxplot(BoxPlot_NPC)
axs[0].set_title('NPC', size=title_size)

axs[1].boxplot(BoxPlot_LCOE, showfliers=False, whis=0)
axs[1].set_title('LCOE', size=title_size)

axs[0].set_xlabel('Households', size=label_size)
axs[0].set_ylabel('NPC (Thousands of USD)', size=label_size)
axs[0].set_xticklabels(range(50,570,50))

axs[1].set_ylim([0.2,0.7])
axs[1].set_xlabel('Households', size=label_size)
axs[1].set_ylabel('LCOE (USD/kWh)', size=label_size)
axs[1].set_xticklabels(range(50,570,50))
plt.subplots_adjust(hspace= 0.4)

plt.savefig('Plots/BoxPlot_LCOE_NPC.png', bbox_inches='tight')    
plt.show()  

# 72
#%%


data_1 = pd.DataFrame()
for i in data.columns:
    foo = data[i]
    foo = foo.sort_values( ascending=False)
    data_1[i] = foo.values
    
index_LDC = []
for i in range(len(data_1)):
    index_LDC.append((i+1)/float(len(data_1))*100)
    
data_1.index = index_LDC    


size = [20,15]
label_size = 25
tick_size = 25 

fig=plt.figure(figsize=size)
ax=fig.add_subplot(111, label="1")
ax2=fig.add_subplot(111, label="2", frame_on=False)

mpl.rcParams['xtick.labelsize'] = tick_size 
mpl.rcParams['ytick.labelsize'] = tick_size 

ax.plot(index_LDC, data_1['Renewable Capacity'], c='y')
ax.plot(index_LDC, data_1['Battery Capacity'], c='g')

ax2.plot(index_LDC, data_1['Renewable Penetration']*100, c='r')
ax2.plot(index_LDC, data_1['Battery Usage Percentage'], c='c')
ax2.plot(index_LDC, data_1['Curtailment Percentage'], c='m')


ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right') 
# limits
ax.set_xlim([0,100])
ax.set_ylim([0,1000])


ax2.set_xlim([0,100])
ax2.set_ylim([0,100])


# labels
ax.set_xlabel('%',size=label_size) 
ax.set_ylabel('Nominal Capacities',size=label_size) 
ax2.set_ylabel('%',size=label_size) 

#NPC = mlines.Line2D([], [], color='b',label='NPC')
#LCOE = mlines.Line2D([], [], color='k',label='LCOE')
Battery_Capacity = mlines.Line2D([], [], color='g',label='Battery nominal capacity (kWh)')
PV_Capacity = mlines.Line2D([], [], color='y',label='PV nominal capacity (kW)')
Renewable_Penetration = mlines.Line2D([], [], color='r',label='Renewable energy penetration')
Battery_Usage = mlines.Line2D([], [], color='c',label='Battery usage')
Energy_Curtailment = mlines.Line2D([], [], color='m',label='Energy curtail')

plt.legend(handles=[
#        NPC, 
#        LCOE, 
        PV_Capacity,
        Battery_Capacity, 
        Renewable_Penetration,
                   Battery_Usage, Energy_Curtailment
 ], bbox_to_anchor=(1, 1),fontsize = 20)

plt.savefig('Plots/Duration_Curve_Capacities.png', bbox_inches='tight')    
plt.show()   

#%%
'hola'

name = 'Renewable Penetration'
data_1 = data.copy()
data_1 = data_1.sort_values(name, ascending=False)

    
# index_LDC = []
# for i in range(len(data_1)):
#     index_LDC.append((i+1)/float(len(data_1))*100)
    
data_1.index = range(1,len(data_1)+1)


size = [20,15]
label_size = 25
tick_size = 25 

fig=plt.figure(figsize=size)
ax=fig.add_subplot(111, label="1")
ax2=fig.add_subplot(111, label="2", frame_on=False)

mpl.rcParams['xtick.labelsize'] = tick_size 
mpl.rcParams['ytick.labelsize'] = tick_size 

ax.plot(range(1,len(data_1)+1) , data_1['Renewable Capacity'], c='y')
ax.plot(range(1,len(data_1)+1) , data_1['Battery Capacity'], c='g')

ax2.plot(range(1,len(data_1)+1) , data_1['Renewable Penetration']*100, c='r')
ax2.plot(range(1,len(data_1)+1) , data_1['Battery Usage Percentage'], c='k')
#ax2.plot(index_LDC, data_1['Curtailment Percentage'], c='m')


ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right') 
# limits
ax.set_xlim([0,1650])
ax.set_ylim([0,1000])


ax2.set_xlim([0,1650])
ax2.set_ylim([0,100])


# labels
ax.set_xlabel('Number of simulations',size=label_size) 
ax.set_ylabel('Nominal Capacities (kW)',size=label_size) 
ax2.set_ylabel('Renewable penetration (%)',size=label_size) 

#NPC = mlines.Line2D([], [], color='b',label='NPC')
#LCOE = mlines.Line2D([], [], color='k',label='LCOE')
Battery_Capacity = mlines.Line2D([], [], color='g',label='Battery nominal capacity (kWh)')
PV_Capacity = mlines.Line2D([], [], color='y',label='PV nominal capacity (kW)')
Renewable_Penetration = mlines.Line2D([], [], color='r',label='Renewable energy penetration')
Battery_Usage = mlines.Line2D([], [], color='k',label='Battery usage')
#Energy_Curtailment = mlines.Line2D([], [], color='m',label='Energy curtail')

plt.legend(handles=[
#        NPC, 
#        LCOE, 
        PV_Capacity,
        Battery_Capacity, 
        Renewable_Penetration,
                   Battery_Usage
#                   , Energy_Curtailment
 ], bbox_to_anchor=(1, 1),fontsize = 20)

plt.savefig('Plots/LDC_Renewable_Penetration.png', bbox_inches='tight')    
plt.show()   

