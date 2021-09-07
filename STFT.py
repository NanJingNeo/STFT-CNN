# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:29:21 2021

@author: 16534
"""

import numpy as np
import scipy.io as sio
from scipy.signal import stft
import matplotlib.pyplot as plt
import cv2


#归一化函数
def normalize(data):
    range = np.max(data)-np.min(data)
    return (data-np.min(data)) / range

# 窗函数
window = 'hamming'
# window = 'hann'
# frame长度
n = 26
overlap=0.9*26
for i in range (1,31):
    directory='./begin/wcc_fall'+str(i)+'.mat'
    savedir='./begin/wcc_fall'+str(i)+'.png'
    #    directory='./begin/wcc_fall30.mat'
    # savedir='./begin/wcc_fall'+str(i)+'.png'
    Data = sio.loadmat(directory)["picS"];  #330*360 
    Data=normalize(Data).flatten()
    Data=Data.transpose()
    
    # STFT
    f, t, Z = stft(Data, fs=1.0, window=window, nperseg=n, noverlap = overlap )
    #列的分辨率为n/2+1
    # 求幅值
    Z = np.abs(Z)
    
    #去除白边
    # plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.pcolormesh(t, f, Z, vmin = 0, vmax = Z.mean())
    plt.savefig(savedir, pad_inches = 0)
    print(i)
























