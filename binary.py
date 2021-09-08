# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:00:06 2021

@author: 16534
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./begin/wcc_fall30.png')

#均值漂移，两个参数分别代表漂移物理空间半径大小；漂移色彩空间半径大小
img2 = cv2.pyrMeanShiftFiltering(img, 22, 255)


GrayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
GrayImage2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(GrayImage2,127,255,cv2.THRESH_BINARY)
# ret,thresh2=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY_INV)
# titles = ['Gray Image','BINARY','BINARY_INV']

# 开运算
# kernel = np.ones((5,5), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))         #定义矩形结构元素
opening_img = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel,iterations=1)

titles = ['Gray Image','BINARY','BINARY_SHIFT', "open"]

images = [GrayImage, thresh1, thresh2, opening_img]

for i in range(4):
   plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()

