import cv2 as ocv
import numpy as np

image = ocv.imread("Ressources/Fermion.jpg")

print(image.shape)

cards = ocv.imread("Ressources/cards.jpg")

cardsResized = ocv.resize(cards, (400, 611)) #Redimmensionner une image (image, (largeur, hauteur))

horizontal = np.hstack((image, cardsResized)) # Concatenation horizontale d'images de même hauteur
print(horizontal.shape)

horizontalResized = ocv.resize(horizontal, (505, 305)) # Redimmension pour diminuer la taille de la fentre des deux images cocnaténées

imageResized = ocv.resize(image, (250, 250)) # Diminution de la taille de l'image pour la concatenation verticale

vertical = np.vstack((imageResized, imageResized)) # Concatenation verticale d'images de même largeur

imageCombo = np.hstack((vertical, vertical))

ocv.imshow("Fermion" ,image)

ocv.imshow("Horizontal", horizontal)

ocv.imshow("HorizontalResized", horizontalResized)

ocv.imshow("Vertical", vertical)

ocv.imshow("Horizontal + Vertical", imageCombo)

ocv.waitKey(0)