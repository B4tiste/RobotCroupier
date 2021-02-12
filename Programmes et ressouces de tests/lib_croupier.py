# -*- coding: utf-8 -*-
"""
Librairie Personelle Croupier

@author: Batiste & Vahe
"""

import os

clear = lambda : os.system('clear')

def ID_card(deck):
    
    carte_1 = deck[0]
    carte_2 = deck[1]
    
    deck.pop(0)
    deck.pop(0)
    
    return deck, carte_1, carte_2

def score(main, tapis):

    #Liste des valeurs que peuvent prendre les cartes
    string_valeurs = "123456789X"
    liste_valeurs = list(string_valeurs)

    
    
    pair = 0
    brelan = 0
    carre = 0
     
    #Conversion des string des mains en liste, afin de pouvoir les éditer
    main.cart_1 = list(main.carte_1)
    main.cart_2 = list(main.carte_2)
    
    #Retrait des couleurs des cartes
    main.cart_1.pop(1)
    main.cart_2.pop(1)
    
    tapis.append(main.cart_1)
    tapis.append(main.cart_2)
    
    print(tapis)
    

def charte_cartes() :
    
    fichier = open("Ressources/list_ID.txt")
    a = fichier.readlines()
    
    print("")
    print("\t" + a[0].rstrip("\n"))
    print("\t" + a[1].rstrip("\n"))
    print("\t" + a[2].rstrip("\n"))
    print("\t" + a[3].rstrip("\n"))
    print("\t" + a[4].rstrip("\n"))
    
    fichier.close()
