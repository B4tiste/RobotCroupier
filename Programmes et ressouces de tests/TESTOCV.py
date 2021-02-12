import cv2 as ocv
import time
from bluedot import BlueDot
from signal import pause

camera = ocv.VideoCapture(0)
webcam = 0
picture = 0

camera.set(3, 640) #Largeur
camera.set(4, 480) #Hauteur
camera.set(10, 200) #Luminosite

fermion = ocv.imread("Ressources/Fermion.jpg")

def trigger(position):
    
    if position.top:
        
        print("Starting Webcam")
        webcam = 1
        
    elif position.bottom:
        
        print("Picture Display")
        ocv.imshow("Fermion", fermion)
        time.sleep(5)
        
    elif position.right:
        
        print("STOP")
        exit()
        

bd = BlueDot()

bd.when_pressed = trigger

pause()