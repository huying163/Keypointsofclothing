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
import cv2

path = r'E:\fashion ai\train\Annotations\train.csv'
dataset = pd.read_csv(path)
idd = r"E:\fashion ai\train"+'\\'+dataset[[0]]
size = 512

def imageDownload(idd):
    #change to tf if needed,idd stores pic locations
    for i in range(len(idd)):
        img=cv2.imread(idd.iloc[i,0])
        if img.shape[0]!=size:
            res=cv2.resize(img,(size,size),interpolation=cv2.INTER_CUBIC)
            print ('image '+str(i)+' has been reshaped to 512*512')
            if not cv2.imwrite(idd.iloc[i,0], res, [int(cv2.IMWRITE_JPEG_QUALITY), 100]):
                print ('failed to save this image,check error')
                break
        else:
            res = img
        #cv2.imshow('preview',img)
        #cv2.imshow('view',res)
        #cv2.waitKey(0)
def imageTransfer(filepath):
    #change to tf if needed,idd stores pic locations
    img=cv2.imread(filepath)
    if img.shape[0]!=size:
        res=cv2.resize(img,(size,size),interpolation=cv2.INTER_CUBIC)    
    else:
        res = img
    return res
def checkSuccess(idd):
    for i in range(len(idd)):
        img=cv2.imread(idd.iloc[i,0])
        if img.shape[0]!=size:
            print ('check error on image number: '+str(i))
            break

    




