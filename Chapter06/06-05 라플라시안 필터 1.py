import cv2
import numpy as np

src = cv2.imread('../lena.jpg', cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(src, ksize=(7,7), sigmaX = 0.0)
cv2.imshow('src',src)
cv2.imshow('blur',blur)

lap= cv2.Laplacian(src,cv2.CV_32F)
minVal, maxVal, minLoc, maxLoc= cv2.minMaxLoc(lap)
dst = cv2.convertScaleAbs(lap)
dst = cv2.normalize(dst,None,0,255,cv2.NORM_MINMAX)
cv2.imshow('lap',lap)
cv2.imshow('dst',dst)

lap2= cv2.Laplacian(blur,cv2.CV_32F)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(lap2)
dst = cv2.convertScaleAbs(lap2)
dst = cv2.normalize(dst,None,0,255,cv2.NORM_MINMAX)
cv2.imshow('lap2',lap)
cv2.imshow('dst2',dst)

cv2.waitKey()
cv2.destroyAllWindows()
