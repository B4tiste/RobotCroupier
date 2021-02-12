# -*- coding: utf-8 -*-
"""
Librairie Personelle Croupier

@author: Batiste & Vahe
"""

def ID_card(deck_rdm):
    
    carte = deck_rdm[0]
    carte_2 = deck_rdm[1]
    
    deck_rdm.pop(0)
    deck_rdm.pop(0)
    
    return deck_rdm, carte, carte_2

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
