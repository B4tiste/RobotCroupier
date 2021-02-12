import cv2 as ocv
import numpy as np

def empty(a):
    pass

path = 'Ressources/Fermion.jpg'
ocv.namedWindow("Trackbars")
ocv.resizeWindow("Trackbars", 680, 240)
ocv.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
ocv.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
ocv.createTrackbar("Saturation Min", "Trackbars", 0, 255, empty)
ocv.createTrackbar("Saturation Max", "Trackbars", 255, 255, empty)
ocv.createTrackbar("Value Min", "Trackbars", 0, 255, empty)
ocv.createTrackbar("Value Max", "Trackbars", 255, 255, empty)

while True:
    image = ocv.imread(path)

    imageHSV = ocv.cvtColor(image, ocv.COLOR_BGR2HSV) # Conversion du RGB au HSV, pour la reconnaissance de couleur

    h_min = ocv.getTrackbarPos("Hue Min", "Trackbars")
    h_max = ocv.getTrackbarPos("Hue Max", "Trackbars")
    s_min = ocv.getTrackbarPos("Saturation Min", "Trackbars")
    s_max = ocv.getTrackbarPos("Saturation Max", "Trackbars")
    v_min = ocv.getTrackbarPos("Value Min", "Trackbars")
    v_max = ocv.getTrackbarPos("Value Max", "Trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = ocv.inRange(imageHSV, lower, upper)



    ocv.imshow("Corgi", image)

    ocv.imshow("Image HSV", imageHSV)

    ocv.imshow("Masque HSV", mask)

    ocv.waitKey(1)