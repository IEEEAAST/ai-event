import cv2 as cv
import numpy as np

def callback(x):
    print("change the value into " + str(x))

src = cv.VideoCapture(0)


cv.namedWindow("output") # create empty window to libk it with the trackbars
cv.createTrackbar('blue higher', "output", 100, 255, callback) # create track bars in the created window
cv.createTrackbar('blue lower', "output", 0, 255, callback) # params(label, output, initial value of the bar, final pos from [0 -> final], callback)

while True:
    ret,frame = src.read() # ret is true if read a thing / frame is the data retrived
    cv.imshow("output",frame)

    if cv.waitKey(1) == ord('q'): #will wait 1ms until refresh, exit using q
        break

    blue_higher = cv.getTrackbarPos("blue higher", "output") #get the position of the bar (with specified label and window)
    blue_lower = cv.getTrackbarPos("blue lower", "output")
    
    mask = cv.inRange(frame,(blue_lower,0,0) , (blue_higher,60,60)) # create the mask range
    cv.imshow("mask",mask) # show mask