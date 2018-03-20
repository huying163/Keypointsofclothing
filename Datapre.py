# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf


dataset = pd.read_csv(r'E:\fashion ai\train\Annotations\train.csv')
idd = r"E:\fashion ai\train"+'\\'+dataset[[0]]
shapecol = []
shapelist = []
size = 512
#imageset= np.zeros((len(idd)/100,size*size*3))
for i in range(len(idd)):
    img=mpimg.imread(idd.iloc[i,0])
    shapecol.append(img.shape[0])
    imgnew = img.reshape((1,-1))
    diffnum = size*size*3 - imgnew.shape[1]
    if diffnum>0:
        imgpad = np.zeros((1,diffnum))
        diff = np.concatenate([imgnew,imgpad],axis=1)
    elif not diffnum:
        diff = img
    else:
        print ("warning:diffnum<0 ")
    shapelist.append(diff)
    if i>100:
        break

testset = dataset.iloc[:102,:]
colname = dataset.columns

test1 = pd.concat([testset,pd.DataFrame(shapelist),pd.DataFrame(shapecol)],axis=1)
#test1.to_csv(r"E:\fashion ai\train\Annotations\abc.csv")




