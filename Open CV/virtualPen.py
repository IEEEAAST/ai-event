import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) 
accumulator_frame = None
while True:
    ret, frame = cap.read()
    fs = frame.shape
    flipped = cv.flip(frame, 1) #flipped to make it easier to understand, like looking in a mirror
    mask = cv.inRange(flipped, (0, 120, 120), (20, 255, 255)) #ranging to find yellow, will return list of either 255 or 0, 255(white) being the color within range, 0(black) being out of range
    
    if accumulator_frame is None:
        accumulator_frame = np.zeros(fs, dtype=np.uint8) #accumulator frame is an empty frame that takes the shape of the main camera frame and is at the start, will update with the drawing

    key_points = np.where(mask) #finds white values in mask and stores it into a list of 2 lists x and y coordinates of the detected color
    x = 0
    y = 0
    length = len(key_points[0]) #returns number of found points that are in the color range
    if length != 0: #to avoid div by zero exception
        for i in range(0,length): #will loop through all the points to get the sum of x and y coordinates
            x += key_points[1][i]
            y += key_points[0][i]
        x = x//length #gets average x
        y = y//length #gets average y
        centroid = (x,y)
        cv.circle(accumulator_frame, centroid, 15, (0, 255, 255), -1) #-1 thickness means the shape is filled

    cv.imshow('result',accumulator_frame | flipped) # | "or" to show both accumulator frame with the drawings + camera flipped view
    cv.imshow('Yellow', mask)
    cv.imshow('Time-Lapse', accumulator_frame)
    if cv.waitKey(1) == ord('q'):
        break