import cv2 as ocv
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)  # Creation d'une image vierge de 512x512, completement noire, en RGB

print(image.shape)

#image[:] = 0, 255, 0  # Colorisation de toute l'image

image[100:200, 250:500] = 0, 0, 150  # Colorisation d'une partie de l'image

ocv.line(image, (489, 54), (300, 150), (0, 255, 0), (3)) # Creation de lignes (Image, depart, arrivée, couleurRGB, epaisseur)

ocv.rectangle(image,(20, 20), (230, 350), (255, 0, 255), 1) # Creation d'un rectangle (Image, depart, arrivée, couleurRGB, epaisseur (ocv.FILLED pour le remplir)

ocv.circle(image,(400, 50), 30, (255, 255, 0), 3) # Creation d'un rectangle (Image, centre, rayon, couleurRGB, epaisseur (ocv.FILLED pour le remplir)

ocv.putText(image, "OPEN CV TEST ", (10, 420), ocv.FONT_HERSHEY_COMPLEX, 2, (255, 255, 150), 2) # Ajout de texte sur l'image (Image, Position de départ, ocv.FONT_XX, taille, couleur, épaisseur)

ocv.imshow("Image", image)

ocv.waitKey(0)
