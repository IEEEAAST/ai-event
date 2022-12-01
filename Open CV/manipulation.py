import cv2 as cv
import numpy as np

def callback(x):
    pass

src = cv.VideoCapture(0)
cv.namedWindow("camera")
cv.createTrackbar('size', 'camera', 1,150,callback)
while True:
    ret,frame = src.read()
    
    size = cv.getTrackbarPos('size', 'camera')
    shape = frame.shape #gets shape of camera frame
    center = (shape[1]//2,shape[0]//2) #shape = (height = y,width = x,#channels) 
    cv.circle(frame,center,size, (0, 0, 255),2) #takes frame to be drawn on, position to draw on,radius,color,thickness
    
    #draw more shapes
    # cv.rectangle(frame,(10,20), (30,40), (0,100,0), 5,)
    # cv.line(frame, (0,0), (50,50),(255,255,255), 4)
    # cv.putText(frame,"AI 101", (100,100), cv.FONT_ITALIC,10,20)
    
    cv.imshow("camera",frame)

    if cv.waitKey(1) == ord('q'):
        break