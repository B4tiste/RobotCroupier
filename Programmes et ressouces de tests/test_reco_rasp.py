import cv2
import numpy as np
import os
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import os

clear = lambda : os.system('clear')

path = 'Cartes'
orb = cv2.ORB_create(nfeatures=1000)

#### Import Images
images = []
classNames = []
myList = os.listdir(path)
print('Total Classes Detected', len(myList))
for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findDes(images):
    desList = []
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList


def findID(img, desList, thres=20):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList = []
    finalVal = -1
    try:
        for des in desList:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            matchList.append(len(good))
    except:
        pass
    # print(matchList)
    if len(matchList) != 0:
        if max(matchList) > thres:
            finalVal = matchList.index(max(matchList))
    return finalVal


desList = findDes(images)
print(len(desList))

cap = cv2.VideoCapture(0)

camera = PiCamera()

resolution = (640, 360)

camera.resolution = resolution
#camera.framerate = 15
rawCapture = PiRGBArray(camera, size=resolution)

time.sleep(0.5)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array
    
    image_originale = image.copy()
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    id = findID(image, desList)
    
    if id != 1:
        cv2.putText(image_originale, classNames[id], (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
        clear()
        print(classNames[id] + '\n\t')
        

    cv2.imshow("Frame", image_originale)
            
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
            
    key = cv2.waitKey(1) & 0xFF
            
    # if the `q` key was pressed, break from the loop
    if key == ord("c"):
            exit()                

time.sleep(0.1)


"""
while True:

    success, img2 = cap.read()
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    id = findID(img2, desList)
    if id != -1:
        cv2.putText(imgOriginal, classNames[id], (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)

    cv2.imshow('img2', imgOriginal)
    cv2.waitKey(1)
"""