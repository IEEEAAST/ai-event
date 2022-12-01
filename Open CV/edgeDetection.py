import numpy as np
import cv2 as cv

img = cv.VideoCapture("D:\Semester 7\opencvdemo\istockphoto-1075392174-640_adpp_is.mp4")
#img = cv.imread('Valorant_RetakeEpisode2CinematicViperScreenshot.jpg')

while True:
    x,frame = img.read()
    grey = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(grey,100,200)

    cv.imshow("edges", edges)
    if cv.waitKey(10) == ord('q'):
        break
    