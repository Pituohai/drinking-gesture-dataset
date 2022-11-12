# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 23:07:19 2022
This is the file that used to:
    1. Import data from pkl file  
    2. Plot IMU signal and the annotation
Before running the code, please change the value of path_x and path_y to the path that save pkl file.
@author: Chunzhuo Wang
"""
#%%
import pandas as pd
import numpy as np
import glob,os
from collections import Counter
import pickle as pkl
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl
import matplotlib.patches as patches
#%%  the path saved the pkl file, you may need to change the path
path_x='D:\\research\\prepared public dataset\\pkl_data\\DX_I_X.pkl'   # change the path for your downloaded dataset
with open(path_x, 'rb') as f:
    dataset = pkl.load(f)
path_y='D:\\research\\prepared public dataset\\pkl_data\\DX_I_Y.pkl'
with open(path_y, 'rb') as f1:
    annoLabel = pkl.load(f1)
#%%  Print information of annotation for each session
for i in range(len(annoLabel)):
    print(Counter(annoLabel[i])) 
#%%
def segment_intervals(Yi):
	idxs = [0] + (np.nonzero(np.diff(Yi))[0]+1).tolist() + [len(Yi)]
	intervals = [(idxs[i],idxs[i+1]) for i in range(len(idxs)-1)]
	return intervals
def segment_labels(Yi):
	idxs = [0] + (np.nonzero(np.diff(Yi))[0]+1).tolist() + [len(Yi)]
	Yi_split = np.array([Yi[idxs[i]] for i in range(len(idxs)-1)])
	return Yi_split
#%%  choose part of the data to visualize
i=0
j=0
for i in range(3,4):
    lengt=12800
    linew=4
    for j in range(5):
        print(i,j)   
        fig, axs = plt.subplots()
        #fig.suptitle('(i,j)')
        fig.set_size_inches(24, 8)
        x = np.linspace(0,lengt,lengt)
        my_x_ticks = np.arange(640, lengt, 640)   
        my_x_ticks1 = np.arange(10, lengt//64, 10) 
        plt.xticks(my_x_ticks,my_x_ticks1, fontsize=15) 
        plt.tick_params(labelsize=20)

        y1 =annoLabel[i][j*lengt:j*lengt+lengt]  # label segment
        a1 =dataset[i][j*lengt:j*lengt+lengt,0]  # acc_x segemnt
        a2 = dataset[i][j*lengt:j*lengt+lengt,1]
        a3 = dataset[i][j*lengt:j*lengt+lengt,2]
        axs.plot(x,a1,label="$acc-x$",color="orange",linewidth=linew)
        axs.plot(x,a2,label="$acc-y$",color="blue",linewidth=linew)
        axs.plot(x,a3,label="$acc-z$",color="green",linewidth=linew)
        axs.set_ylim([-60, 20])
        #axs.set_title(str(j))
        axs.set_ylabel('Acceleration (m/$s^2$)', fontsize=20)
        axs.set_xlabel('time (s)', fontsize=20)
        axs.spines['top'].set_visible(False)
        axs1=axs.twinx()
        axs1.set_ylim([-5, 15])
        axs1.set_ylabel('Angular velocity (rad/s)', fontsize=20)
        axs1.spines['top'].set_visible(False)
        axs1.spines['left'].set_linewidth(4)
        axs1.spines['right'].set_linewidth(4)
        axs1.spines['bottom'].set_linewidth(4)
        axs.spines['left'].set_linewidth(4)
        axs.spines['right'].set_linewidth(4)
        axs.spines['bottom'].set_linewidth(4)
        g1 = dataset[i][j*lengt:j*lengt+lengt,3]*3.14/180   # gyro_x segment
        g2 = dataset[i][j*lengt:j*lengt+lengt,4]*3.14/180
        g3 = dataset[i][j*lengt:j*lengt+lengt,5]*3.14/180
        axs1.plot(x,g1,label="$gyro-x$",color="black",linewidth=linew)
        axs1.plot(x,g2,label="$gyro-y$",color="red",linewidth=linew)
        axs1.plot(x,g3,label="$gyro-z$",color="teal",linewidth=linew)
        axs1.tick_params(labelsize=20)
        true_intervals_id = np.array(segment_intervals(y1))
        true_labels_id = segment_labels(y1)
        bg_class=0
    # Remove background labels
        if bg_class is not None:
            true_intervals_id = true_intervals_id[true_labels_id!=bg_class]
            true_labels_id = true_labels_id[true_labels_id!=bg_class]
    
        max_acc = np.max(np.abs(a1))
        for k, gt in enumerate(true_intervals_id):
            width = gt[1] - gt[0]
            pos_acc = (gt[0], -max_acc)
            height_acc = 80
            if k == 0:
                axs1.add_patch(patches.Rectangle(pos_acc, width,
                                                height_acc, edgecolor=None, facecolor='grey', alpha=0.5, label='drinking gesture'))
            else:
                axs1.add_patch(patches.Rectangle(pos_acc, width,
                                                height_acc, edgecolor=None, facecolor='grey', alpha=0.5))
        #axs.legend(loc='upper left',fontsize=15)
        #axs1.legend(fontsize=15)
        axs1.legend(bbox_to_anchor=(1.1,1), loc="upper left", fontsize=15)
        axs.legend(bbox_to_anchor=(1.1,0), loc="upper left", fontsize=15)
#%%
