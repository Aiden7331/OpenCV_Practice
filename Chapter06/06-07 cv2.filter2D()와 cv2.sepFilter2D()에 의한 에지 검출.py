import cv2
import numpy as np

src = cv2.imread('../lena.jpg', cv2.IMREAD_GRAYSCALE)

#1
kx, ky =cv2.getDerivKernels(1,0,ksize=3)
sobelX=ky.dot(kx.T)
print('kx=',kx)
print('ky=',ky)
print('sobelX=',sobelX)
gx = cv2.filter2D(src,cv2.CV_32F,sobelX)

kx,ky = cv2.getDerivKernels(0,1,ksize=3)

