import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('../lena.jpg',cv2.IMREAD_GRAYSCALE)

hist1 = cv2.calcHist(images=[src], channels=[0], mask=None, histSize=[32], ranges=[0,256])
hist2 = cv2.calcHist(images=[src], channels=[0], mask=None, histSize=[256], ranges=[0,256])

hist1=hist1.flatten()
hist2=hist2.flatten()

#1
plt.title('hist1: binX = np.arange(32)') # plt 그래프 타이틀 설정
plt.plot(hist1,color='r')
binX= np.arange(32)
plt.bar(binX,hist1,width=1,color='b')
plt.show()

#2
plt.title('hist1: binX = np.arange(32) * 8') # plt 그래프 타이틀 설정
plt.plot(hist1,color='r')
binX= np.arange(32)*8
plt.bar(binX,hist1,width=8,color='b')
plt.show()

cv2.imshow('src',src)

#3
plt.title('hist2: binX = np.arange(256)') # plt 그래프 타이틀 설정
plt.plot(hist2,color='r')
binX= np.arange(256)
plt.bar(binX,hist2,width=1,color='b')
plt.show()