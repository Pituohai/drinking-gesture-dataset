# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 09:40:02 2022
This is the file used to:
    1. Import data from .csv file  
    2. Generate .pkl file
Before running the code, please change: 
    1. the folder path save the DX dataset
    2. the path planned to save pkl file
@author: Chunzhuo Wang
"""
#%%
import pandas as pd
import numpy as np
import glob,os
from collections import Counter
import pickle as pkl

#%% operate DX-I file, you may need to change the path

path=r'D:\research\drinking dataset\DX1\DX-I\Hand-Mirrored'
file=glob.glob(os.path.join(path, "*.csv"))      
print(file) # the file_path list
data_intotal=[] # list to save 6-axis IMU data
target_intotal=[] # list to save annotation
for f in file:
  dl= []
  dl.append(pd.read_csv(f))     #
  df=pd.concat(dl)
  df = df.drop(['t'],axis=1) # IMU data
  target1 = df.pop('anno')   # annotation 
  target1=target1.values
  data_set=df.values
  data_intotal.append(data_set)
  target_intotal.append(target1)     
for i in range(len(target_intotal)):
    print(Counter(target_intotal[i]))
#%%    
with open('D:\\research\\public dataset\\pkl_data\\DX_I_X.pkl', 'wb') as f:  # change the path to save data-X pkl
   pkl.dump(data_intotal, f)
with open('D:\\research\\public dataset\\pkl_data\\DX_I_Y.pkl', 'wb') as f:  # change the path to save data-Y pkl
   pkl.dump(target_intotal, f)

#%%  operate DX-II files, you may need to change the path

path=r'D:\research\drinking dataset\DX2\DX-II\Hand-Mirrored'
file=glob.glob(os.path.join(path, "*.csv"))      
print(file)
data_intotal=[]
target_intotal=[]
for f in file:
  dl= []
  dl.append(pd.read_csv(f))     #
  df=pd.concat(dl)
  df = df.drop(['t'],axis=1)
  target1 = df.pop('anno')
  target1=target1.values
  data_set=df.values
  data_intotal.append(data_set)
  target_intotal.append(target1)     
for i in range(len(target_intotal)):
    print(Counter(target_intotal[i]))
#%%
with open('D:\\research\\public dataset\\pkl_data\\DX_II_X.pkl', 'wb') as f:
   pkl.dump(data_intotal, f)
with open('D:\\research\\public dataset\\pkl_data\\DX_II_Y.pkl', 'wb') as f:
   pkl.dump(target_intotal, f)
