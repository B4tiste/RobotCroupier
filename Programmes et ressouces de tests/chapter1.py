import cv2 as ocv
import numpy as np

print("Import success")

#Camera

camera = ocv.VideoCapture(0)
camera.set(3, 640) #Largeur
camera.set(4, 480) #Hauteur
camera.set(10, 50) #Luminosité



while True:
    success, img = camera.read()

    if success:

        cameraContours = ocv.Canny(img, 75, 75)

        imageLudo = cameraContours.copy()

        kernel = np.ones((3, 3), np.uint8)
        ocv.erode(imageLudo, kernel)
        ocv.dilate(imageLudo, kernel)

        cameraFloue = ocv.GaussianBlur(img, (11, 11), 0)

        cameraCF = ocv.Canny(cameraFloue, 25, 25)

        cameraGrise = ocv.cvtColor(img, ocv.COLOR_BGR2GRAY)

        ocv.putText(cameraContours, "Contours ", (10, 420), ocv.FONT_HERSHEY_COMPLEX, 2, (255, 255, 150), 2)
        ocv.putText(cameraCF, "Josh ", (10, 420), ocv.FONT_HERSHEY_COMPLEX, 2, (255, 255, 150), 2)
        ocv.putText(imageLudo, "Ludo ", (10, 420), ocv.FONT_HERSHEY_COMPLEX, 2, (255, 255, 150), 2)

        horizontal = np.hstack((cameraContours, cameraCF, imageLudo))

        ocv.imshow("Contours", cameraContours)

        ocv.imshow("Contours+Floue", cameraCF)

        ocv.imshow("Webcam", img)

        ocv.imshow("Grise", cameraGrise)

        ocv.imshow("Ludo", imageLudo)

        ocv.imshow("Horizontal", horizontal)

        if ocv.waitKey(1) & 0xFF ==ord('c'):
            break