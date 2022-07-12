# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:23:56 2021

@author: Jonathan.X
"""
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

os.chdir(r"***workspace\python")
#%%
exp = pd.read_csv(r'bodyfat.csv', encoding="utf-8")
exp.head()
#%%
exp.plot('Density','BodyFat',kind='scatter')

plt.show()
#%% read the data from excel,check the total number
datall = pd.read_csv('bodyfat.csv')
print("%d",datall.shape[0])
#%% check the descibe
data1 = datall
data1.describe(include = 'all').T

#%% check bins
matplotlib.rcParams['axes.unicode_minus']=False
data1.BodyFat.hist(bins = 50)

plt.xlabel("bodyfat chart")
plt.ylabel('total')

#%%  check the max  min and bins / mid median ,mean
print(data1.BodyFat.agg(['mean','median','std']))
print(data1.BodyFat.quantile([0.25,0.5,0.75]))
#%% check the max and min  sample in group
pd.concat([(data1[data1.BodyFat==min(data1.BodyFat)]),data1[data1.BodyFat==max(data1.BodyFat)]])
'''
Y Value  we all have finished  researched ,then we must continue to research the X value
we must observe  the  X  value belong to which kind of variables? generally Categorical variables and series variable type
in this case ,all variables are series type,so we reseach them, first columne is the number consequbtly ,so we do not need them
all 15 columns

for i in range(15):
    if i !=0:
        print(data1.columns.values[i],":")
        print(data1[data1.columns.values[i]].agg(['value_counts']).T)
        print("===================================================")
    else:
        continue

if the there are categorical variables left ,we can print them out for their data characteristics
 for example 
 print(data1.+++++++)
''' 
#%%
exp.plot('BodyFat','Weight',kind='scatter')
plt.show()
#%%
exp.plot('BodyFat','Age',kind='scatter')

plt.show()
#%%
exp.plot('BodyFat','Height',kind='scatter')

plt.show()
#%%
exp.plot('BodyFat','Abdomen',kind='scatter')
plt.show()
#%%
exp.plot('BodyFat','Hip',kind='scatter')
plt.show()
#%%
exp.plot('BodyFat','Chest',kind='scatter')
plt.show()

#%%
exp.plot('BodyFat','Ankle',kind='scatter')
plt.show()
#%%
exp[['BodyFat','Age','Weight','Height','Density','Abdomen','Neck','Thigh','Knee','Biceps','Forearm','Wrist','Hip','Chest','Ankle']].corr(method='pearson')
#%%
lm_s = ols('BodyFat ~ Age + Weight + Height + Density + Abdomen + Neck + Thigh + Knee + Biceps + Forearm + Wrist + Hip + Chest +Ankle', data=exp).fit()
lm_s.summary()

#%%
pd.DataFrame([lm_s.predict(exp),lm_s.resid],index=['predic','resid']).T.head()

#%%
lm_sm = ols('BodyFat ~ + Density + Wrist + Height', data=exp) 

lm_s = lm_sm.fit()

lm_s.summary()
#%%
def forward_select(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float('inf'), float('inf')
    while remaining:
        aic_with_candidates=[]
        for candidate in remaining:
            formula = "{} ~ {}".format(
                response,' + '.join(selected + [candidate]))
            aic = ols(formula=formula, data=data).fit().aic
            aic_with_candidates.append((aic, candidate))
        aic_with_candidates.sort(reverse=True)
        best_new_score, best_candidate=aic_with_candidates.pop()
        if current_score > best_new_score: 
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
            print ('aic is {},continuing!'.format(current_score))
        else:        
            print ('forward selection over!')
            break
            
    formula = "{} ~ {} ".format(response,' + '.join(selected))
    print('final formula is {}'.format(formula))
    model = ols(formula=formula, data=data).fit()
    return(model)
#%%
data_for_select = exp[['BodyFat','Age','Weight','Height','Density','Abdomen','Neck','Thigh','Knee','Biceps','Forearm','Wrist','Hip','Chest','Ankle']]
    
lm_m = forward_select(data=data_for_select, response='BodyFat')
print(lm_m.rsquared ,'= R2')