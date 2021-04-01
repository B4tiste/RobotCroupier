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
import RPi.GPIO as GPIO


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


# Definition des pins
M1_En = 21
M1_In1 = 20
M1_In2 = 16

M2_En = 18
M2_In1 = 23
M2_In2 = 24


# Creation d'une liste des pins pour chaque moteur pour compacter la suite du code
Pins = [[M1_En, M1_In1, M1_In2], [M2_En, M2_In1, M2_In2]]
#Pins = [[M1_En, M1_In1, M1_In2]]

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)

GPIO.setup(M2_En, GPIO.OUT)
GPIO.setup(M2_In1, GPIO.OUT)
GPIO.setup(M2_In2, GPIO.OUT)


# Voir aide dans le tuto
M1_Vitesse = GPIO.PWM(M1_En, 50)
M2_Vitesse = GPIO.PWM(M2_En, 50)
M1_Vitesse.start(100)
M2_Vitesse.start(100)


def sens1(moteurNum) :
    GPIO.output(Pins[moteurNum - 1][1], GPIO.HIGH)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    #print("Moteur", moteurNum, "tourne dans le sens 1.")


def sens2(moteurNum) :
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.HIGH)
    #print("Moteur", moteurNum, "tourne dans le sens 2.")

def arret(moteurNum) :
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    #print("Moteur", moteurNum, "arret.")

def arretComplet() :
    GPIO.output(Pins[0][1], GPIO.LOW)
    GPIO.output(Pins[0][2], GPIO.LOW)
    GPIO.output(Pins[1][1], GPIO.LOW)
    GPIO.output(Pins[1][2], GPIO.LOW)
    #print("Moteurs arretes.")
    arretComplet()

def tournemoteur() :

    print('Distribution')
    load_bar(0.5)

    sens1(1)
    time.sleep(0.5)
    arret(1)
    time.sleep(0.3)




