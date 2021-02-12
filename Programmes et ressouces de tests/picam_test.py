# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()

resolution = (640, 360)

rgb_fps = (255, 0, 255)

camera.resolution = resolution
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=resolution)

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array
    
    #Initialisation de mon compteur de FPS
    tickmark = cv2.getTickCount()
    
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    
    #cv2.putText(image, "FPS : {:05.2f}".format(fps), (100, 50), cv2.FONT_HERSHEY_PLAIN, 1.0, rgb_fps, 2)
		
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
    # if the `q` key was pressed, break from the loop
    if key == ord("c"):
        exit()