import cv2
import numpy as np

image = cv2.imread("Ressources/Fermion.jpg")

corgi = cv2.imread("Ressources/Corgi.jpg")

kernel = np.ones((5, 5), np.uint8)

imageGrise = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Conversion de l'image RGB en niveau de Gris

imageFloue = cv2.GaussianBlur(imageGrise, (11,11), 0) #Floutage de l'image en gris

imageContour = cv2.Canny(image, 100, 100) #Detection des contours de l'image

#imageCorgi = cv2.Canny(corgi, 150, 150)

imageDilatation = cv2.dilate(imageContour, kernel, iterations=1) #Dilatation des contours detectés

imageErosion = cv2.erode(imageDilatation, kernel, iterations=1) #Erosion des contours de l'image


cv2.imshow("Image de Base", image)

cv2.imshow("Image Grise", imageGrise)

cv2.imshow("Image grise Floue", imageFloue)

cv2.imshow("Contours de l'image", imageContour)

cv2.imshow("Dilatation des contours", imageDilatation)

cv2.imshow("Erosion des contours", imageErosion)

#cv2.imshow("Contours Corgi", imageCorgi)

cv2.waitKey(0)