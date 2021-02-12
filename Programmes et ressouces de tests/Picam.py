#import des bibiliothèques nécessaires
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as ocv

#Initialisation de la camera et récupération du chemin de récupréation des images capturées
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
rawCapture = PiRGBArray(camera, size = (640, 480))

#Laisser la cam démarrer
time.sleep(0.1)

#Recupération des frames de la camera

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    #Recupération de la représentation de la frame
    
    image = frame.array
    
    #Afficher la frame
    ocv.imshow("Frame", image)
    key = ocv.waitKey(0) & 0xFF
    
    #Clear du flux afin d'afficher la prochaine frame
    rawCapture.truncate(0)
    
    #Arret lors d'un appui sur c
    if key == ord("q"):
        break

