import cv2 as cv
import numpy as np

def callback(x):
    print(x)

src = cv.VideoCapture(0)

cv.namedWindow("circle")
cv.createTrackbar('radius', 'circle', 105, 1500, callback)
while True:
    ret,frame= src.read()
    img = cv.flip(frame,1)
    
    dim = img.shape


    center=(dim[1]//2,dim[0]//2)
    clr = (0,0,255)
    rad = cv.getTrackbarPos('radius', 'circle')
    cv.circle(img,center,rad,clr,cv.FILLED)
    #cv.putText(img,"AI101",(50,250),cv.FONT_HERSHEY_PLAIN,10,(0,255,0), 5)
    mask = cv.inRange(img,(0,0,200),(0,0,255))

    grey= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    edge = cv.Canny(grey,5,200)

    cv.imshow("canny img",edge)
    cv.imshow("mask",mask)
    cv.imshow("circle",img)
    if cv.waitKey(1) == ord('q'):
        break
    