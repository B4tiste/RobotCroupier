# -*- coding: utf-8 -*-
"""
Projet ER3-PT3 : Croupier 

    Création du jeu de poker autonome (sans cam), avec base de données de 52 cartes

@author: batis
"""

import lib_croupier
import random
import os
import cv2
import time

clear = lambda : os.system('cls')

clear()

#     Creation de la classe Cartes
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
    def __init__(self, name, carte_1, carte_2, debout, cote):
        self.name = name
        self.carte_1 = carte_1
        self.carte_2 = carte_2
        self.debout = debout
        self.cote = cote
        
#        def Affectation_main(self):

#Initialisation des objets joueurs (Name, carte_1, carte_2, debout, position)
j1 = Joueur("Joueur_1","","","","")
j2 = Joueur("Joueur_2","","","","")
j3 = Joueur("Joueur_3","","","","")
j4 = Joueur("Joueur_4","","","","")
j5 = Joueur("Joueur_5","","","","")

#Mise en liste de tous les joueurs
liste_joueur = [j1, j2, j3, j4, j5]

#Ajout du PATH de la base de données des cartes
path = "Cartes"
#orb = cv2.ORB_create(nfeatures=1000)

#Initialisation des images de chaque cartes
images = []

#Initialisation des decks de cartes
deck_initial = []

#Creation d'un tableau vide de 52 cases
deck_jeu = []
for t in range(52):
    deck_jeu.append("")

myList = os.listdir(path)

#Création du paquet de carte

print('\n\t\t===INITIALISATION===')
print('\nNombes de cartes detectées : ', len(myList))

for cl in myList :
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    deck_initial.append(os.path.splitext(cl)[0])

print("\n Liste des cartes detectées dans la base de données de cartes : \n\n" + str(deck_initial).replace("'",""))

print("\n\t===== POKER =====\n\n\t")

#Affichage de la liste des joueurs
print("Liste des joueurs : ")
for e in range(len(liste_joueur)):
    print(liste_joueur[e].name)

#Affichage du deck
print("\nDeck : \n" + str(deck_initial))

#Affectation case par case des variables de "deck_inital" dans "deck_jeu"
#Méthode case par case afin de ne pas rencontrer de problème des mémoire

length = int(len(deck_initial))
for i in range(length):
    deck_jeu[i] = deck_initial[i]

#Affichage de la taille du deck
print("\nTaille du deck : " + str(length))
    
x = int(length/2)

'''
l.106 :
Utilisation de la fonction ID_card présente dans la 'bvf', la bibliothèque contenant toutes
    les fonctions de notre projet
    
    ID_card permet de récupérer les deux premières cartes du deck de jeu qui lui est donné
        en paramètre. Il est question d'exploiter la fonctionnalité de 'multi-return' de
        python, nous permettant d'extraire plusieurs variables traitées dans une fonctionss
        au sein d'un tableau de taille n*return (C'est principalement grâce à cette
        fonctionnalités que les pointeurs sont absents du langage Python)

l.117 :
On affecte aussi les deux cartes aux mains des joueurs, en fonction de l'itération
    à laquelle se trouve la boucle FOR
    
    Les cartes composants la main du Joueur n°i se trouve dans :
        liste_joueurs[i].carte_1
        liste_joueurs[i].carte_2
    Sachant que les éléments de la liste_joueurs sont des objets

l.121 :
On affiche l'état du paquet après chaque retrait, puisque les cartes sont retirées de celui-ci

l.128 :
Puis affectation du nouveau paquet pour la prochaine itération

Condition de la boucle for :
Le nombre d'itération de la boucle est x = (taille du paquet)/2, puisque l'on retire 2 cartes
    à chaque fois
'''

for i in range(x):
    
    if i == len(liste_joueur):
        break
    else:
    
        deck_jeu = list(lib_croupier.ID_card(list(deck_jeu)))
        
        print("\n\tTirage n°" + str(i+1))
        
        liste_joueur[i].carte_1 = deck_jeu[1]
        liste_joueur[i].carte_2 = deck_jeu[2]
        
        if deck_jeu[0] == [] :
            print("Paquet vide ! \n")
        else:
            print("5 premières cartes du paquet après retrait des deux cartes : \n")
            print(deck_jeu[0][0:5])
        
        deck_jeu = deck_jeu[0]

print()

#Création du tapis
print("\t===TAPIS===")

tapis = []

#Ajout d'une carte à la liste "tapis"
#Retrait de chaque carte dans le deck de jeu
for i in range(5):
    
    tapis.append(deck_jeu[i])
    
    deck_jeu.pop(i)


#Affichage du tapis
print(tapis)

print()

#Affichage des mains des joueurs :
for n in range(x):
    
    if n == len(liste_joueur):
        break
    else:
        print("Main du joueur n°" + str(n+1) + " : " + str(liste_joueur[n].carte_1) + " " + str(liste_joueur[n].carte_2))


print()

#Affichage du deck après toute la distribution
print("\t==DECK APRES DISTRIBUTION MAIN + TAPIS==\n")
print(str(deck_jeu).replace("'",""))
print("Taille : " + str(len(deck_jeu)) + " cartes")

print()

'''
lettre = input("Entrer a pour continuer : ")


if lettre == 'a':
    print("Fermeture du programme dans 5 secondes \n")
    time.sleep(5)
else:
    exit()
'''