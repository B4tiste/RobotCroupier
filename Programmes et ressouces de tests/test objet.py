# -*- coding: utf-8 -*-
"""
Librairie de Batiste

@author: batis
"""

# import the necessary packages
# from picamera.array import PiRGBArray
# from picamera import PiCamera
import time
import cv2
import numpy as np


# Image de fond de la liste des ID des couleurs et valeurs de cartes
image = cv2.imread("Ressources/black.jpg")

fichier = open("Ressources/list_ID.txt")
a = fichier.readlines()

# Ajout du texte des ID sur le fond noir
# Ajout de texte sur l'image (Image, Position de départ, ocv.FONT_XX, taille, couleur, épaisseur)
cv2.putText(image, a[0].rstrip("\n"), (10, 35), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 150), 2)
cv2.putText(image, a[1].rstrip("\n"), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 150), 2)
cv2.putText(image, a[2].rstrip("\n"), (10, 105), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 150), 2)

# Affichage de la fenetre
cv2.imshow("Liste_ID", image)

cv2.waitKey(0)

#     Creation de la classe Robot
#     Affectation des arguments des objets liés à cette classe
#     Self -->"Self affectation"
class Carte:
    def __init__(self, valeur, couleur, position):
        self.valeur = valeur
        self.couleur = couleur
        self.position = position
        
    # Creation des "methodes" = Fonctions propres
    # OBJET.fonction --> execution de la routine
#        def change_pos(self):

class Joueur:
    def __init__(self, carte_1, carte_2, debout, cote):
        self.carte_1 = carte_1
        self.carte_2 = carte_2
        self.debout = debout
        self.cote = cote
        
#        def Affectation_main(self):
         



