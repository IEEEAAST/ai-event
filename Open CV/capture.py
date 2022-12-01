import cv2 as cv
import numpy as np

#src = cv.VideoCapture('istockphoto-1075392174-640_adpp_is.mp4')
src = cv.VideoCapture(0)
while True:
    ret,frame = src.read() # ret is true if read a thing / frame is the data retrived

    cv.imshow("output",frame) #imshow displays frame output from .read
    if cv.waitKey(10) == ord('q'): #will wait 1ms until refresh, exit using q
        break