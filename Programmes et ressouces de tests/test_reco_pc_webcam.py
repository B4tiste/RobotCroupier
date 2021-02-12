# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:48:15 2020

@author: batis
"""

import cv2
import numpy as np
import os
import pyperclip

clear = lambda : os.system('cls')

path = 'Cartes'
orb = cv2.ORB_create(nfeatures=1000)

clear()

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


def findID(img, desList, thres=35):
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

while True:
    
    #FPS
    tickmark=cv2.getTickCount()
    
    success, img2 = cap.read()
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    id = findID(img2, desList)
    if id != -1:
        cv2.putText(imgOriginal, classNames[id], (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 2)
    
    #FPS
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(imgOriginal, "FPS: {:05.2f}".format(fps), (20, 80), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), 2)

    
    cv2.imshow('Detection Carte', imgOriginal)
    
    key = cv2.waitKey(1) & 0xFF
            
    # if the `c` key was pressed, break from the loop
    if key == ord("c"):
        
        exit()
    
    
    
