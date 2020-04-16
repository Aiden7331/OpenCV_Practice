import numpy as np
import cv2

width,height=512, 512
x,y,R = 256,256,50
direction=0

while True:
    key = cv2.waitKeyEx(30)
    if key == 0x1B: # no key down
        break;


    #키 읽어오기
    elif key == 0x250000: # left
        direction=1
    elif key == 0x260000: # up
        direction=2
    elif key == 0x270000: # right
        direction=3
    elif key == 0x280000: # down
        direction=4

    #이동하기
    if direction == 1:
        x-=10
    elif direction == 2:
        y-=10
    elif direction == 3:
        x+=10
    elif direction == 4:
        y+=10

    #경계확인하기
    if x < R:
        x=R
        direction = 3
    if x > width -R:
        x = width - R
        direction = 1
    if y < R:
        y = R
        direction = 4
    if y > height - R:
        y = height - R
        direction = 2

    # 지우고 그리기
    img = np.zeros((width, height, 3), np.uint8)+255 #지우기
    cv2.circle(img,(x,y),R,(0,0,255),-1)
    cv2.imshow('img',img)

cv2.destroyAllWindows()