import cv2 as cv
import numpy as np

board = None
src = cv.VideoCapture(0)
while True:
    p,img = src.read()
    img = cv.flip(img,1)

    if board is None:
        dim = img.shape
        board = np.zeros(dim,dtype=np.uint8)
    1
    lower = (0,120,120)
    upper = (30,255,255)
    mask = cv.inRange(img,lower,upper)

    pos = np.where(mask)
    num = len(pos[0])
    if(num!=0):
        avg_x=0
        avg_y=0
        for idx in range(num):
            avg_x += pos[1][idx]
            avg_y += pos[0][idx]
        avg_x = avg_x//num
        avg_y = avg_y//num

        cv.circle(board, (avg_x,avg_y), 15,(0, 255,255),cv.FILLED)
    
    cv.imshow("or",img|board)
    cv.imshow("and",img&board)
    cv.imshow("mask",mask)
    if cv.waitKey(1) == ord('q'):
        break