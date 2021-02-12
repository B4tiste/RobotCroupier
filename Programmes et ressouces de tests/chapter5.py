import cv2 as ocv
import numpy as np

image = ocv.imread("Ressources/cards.jpg")

width, height = 250, 350


pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]]) # Ensemble de 4 points positionnés au 4 coins de la carte Roi de Pique

pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]]) # Assignation des coiuns dans l'ordre

matrix = ocv.getPerspectiveTransform(pts1, pts2) # Matrice des différents points de la carte

imageCarte = ocv.warpPerspective(image, matrix, (width, height)) # Fusion de la matrice (masque) et l'image des cartes

imageContoursCarte = ocv.Canny(imageCarte, 100, 100)

ocv.imshow("Cartes", image)
ocv.imshow("Roi de pique", imageCarte)
ocv.imshow("Contours Roi de pique", imageContoursCarte)

ocv.waitKey(0)