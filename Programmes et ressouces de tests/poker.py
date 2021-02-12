# -*- coding: utf-8 -*-
"""
Projet ER3-PT3 : Croupier 

    Création du jeu de poker

@author: batiste
"""

# from picamera.array import PiRGBArray
# from picamera import PiCamera
import time
import cv2
import numpy as np
import os
import bvf
import random

clear = lambda : os.system('clear')

path = "Cartes"
orb = cv2.ORB_create(nfeatures=1000)

images = []
deck_initial=[]

myList = os.listdir(path)

clear()

print('\n\t\t===INITIALISATION===')
print('\nNombes de cartes detectées : ', len(myList))

for cl in myList :
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    deck_initial.append(os.path.splitext(cl)[0])

print("\n Liste des cartes : \n\n" + str(deck_initial).replace("'",""))

# Image de fond de la liste des ID des couleurs et valeurs de cartes
#image = cv2.imread("Ressources/black.jpg")

# Ajout du texte des ID sur le fond noir
# Ajout de texte sur l'image (Image, Position de départ, ocv.FONT_XX, taille, couleur, épaisseur)
#cv2.putText(image, a[0].rstrip("\n"), (10, 35), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 150), 2)
#cv2.putText(image, a[1].rstrip("\n"), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 150), 2)
#cv2.putText(image, a[2].rstrip("\n"), (10, 105), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 150), 2)

# Affichage de la fenetre
#cv2.imshow("Liste_ID", image)

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
   


    
        #Main

print("\n\t Debut du jeu")

deck_random = deck_initial

random.shuffle(deck_random)

print("\n Deck mélangé : \n" + str(deck_random).replace("'",""))

#print("\n Deck initial, après le mélange de deck_m : \n" + str(deck_initial).replace("'",""))

ID_carte = lib.ID_card(deck_random)
deck_random = ID_carte[0]
carte_random = ID_carte[1]

print("\n\t Longueur du nouveau deck : " + str(len(deck_random)))
#print("\n Nouveau deck : " + str(deck_random))
#print("\n Deck après retrait de la carte selctionnée : " + str(deck_initial))
print("\n\t Carte aléatoire : " + carte_random)

#lib.charte_cartes()

#if cv2.waitKey(1) & 0xFF ==ord('c'):
#    
#    exit()



            