# -*- coding: utf-8 -*-
"""
Librairie Personelle

@author: batis
"""

import time
import progressbar
import os
import pyshorteners
import pyperclip
from getpass import getpass

clear = lambda : os.system('cls')

delay = 2

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

def link_short():
    link = input('\n\tLien a rétrecir : ', )

    shortener =  pyshorteners.Shortener()

    lien_short = shortener.tinyurl.short(link)

    print("\n\t l'url : " + lien_short + ' a été copié dans le presse-papier')

    pyperclip.copy(lien_short)

    return lien_short

def load_bar(t) : 	
	
    for i in progressbar.progressbar(range(100)):
        time.sleep(t/100)
	
def scan_login():
    
    #clear()
    
    x = 0
    
    for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if os.access(lettre + ":\\", os.R_OK):
            x = 1
            if os.access(lettre + ":\\" + "login.txt", os.R_OK):
                print("\nClé de login trouvée sur :", lettre + ":\\")
                print("\n\tAutorisation accordée, débloquage dans " + str(delay) + " secondes...\n")
                x = 2
                load_bar(delay)
            else :
                print('\n\tAucun login detecté sur : ' + lettre + ":\\")
                load_bar(0.5)
                
        if x==1 and lettre =='Z' :
            print('\n\tAutorisation par clé non-accordée !\n\tMot de passe ADMIN requis : ')
            mdp = getpass('\t\tMot de passe : ')
            
            if mdp == 'batiste14' :
                clear()
                print("\n\tMot de passe correct, débloquage dans " + str(delay) + " secondes...\n")

                load_bar(delay)
                
            else :
                clear()
                print("\n\tMot de passe faux, fermeture du programme dans " + str(delay) + " secondes...")
                load_bar(delay)
                clear()
                exit()
