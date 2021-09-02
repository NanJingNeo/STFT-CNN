# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:29:21 2021

@author: 16534
"""

import numpy as np
import scipy.io as sio
from scipy.signal import stft
import matplotlib.pyplot as plt

def normalize(data):
    range = np.max(data)-np.min(data)
    return (data-np.min(data)) / range

# 窗函数
window = 'hann'
# frame长度
n = 26
overlap=0.8*26

Data = sio.loadmat('./begin/wcc_fall3.mat')["picS"];  #330*360 

Data=normalize(Data).flatten()
Data=Data.transpose()


# STFT
f, t, Z = stft(Data, fs=1.0, window=window, nperseg=n, noverlap = overlap )
# 求幅值
Z = np.abs(Z)
# # # 如下图所示
plt.pcolormesh(t, f, Z, vmin = 0, vmax = Z.mean()*10)

# plt.colorbar()