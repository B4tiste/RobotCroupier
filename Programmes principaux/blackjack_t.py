# -*- coding: utf-8 -*-
"""
Code du Jeu Blackjack

@author: batiste
"""

import time
import os
import random
import lib

clear = lambda : os.system('cls')

clear()

delay = int(input("\n Durée des temps de chargement en secondes : "))

class Joueur:
	def __init__(self, name, main, blackjack):
		self.name = name
		self.main = main
		self.blackjack = blackjack

def jeu() :
	#Création du deck de cartes de jeu du blackjack
	deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12 , 13, 14]*4
	#print(deck)

	#Initialisation des objets joueurs avec DEALER = 0  (Name, main, blackjack)
	dealer = Joueur("Dealer",[],0)

	j1 = Joueur("Joueur_1",[],0)
	j2 = Joueur("Joueur_2",[],0)
	j3 = Joueur("Joueur_3",[],0)
	j4 = Joueur("Joueur_4",[],0)
	j5 = Joueur("Joueur_5",[],0)

	#Mise en liste de tous les joueurs possibles
	liste_joueurs = [dealer, j1, j2, j3, j4, j5]

	#Dans le cas d'un nombre de joueur variable
	nbr_joueurs = int(input("\nEntrer le nombre de joueurs : "))

	#Dans le cas d'un nombre de joueurs fixé
	#nbr_joueurs = 2
	
	if nbr_joueurs > len(liste_joueurs)-1:
		print("\n NOMBRE DE JOUEURS TROP GRAND")
		print("\n Reboot dans 5 secondes...\n\n")
		
		lib.load_bar(5)
		
		clear
		
		jeu()

	clear()

	#====================FONCTIONS====================

	#Fonction permettant de récupérer une carte depuis le paquet
	#A changer si on récupère l'input depuis la cam
	def tirage_carte():
		
		carte = random.choice(deck)
		
		deck.remove(carte)
		
		if carte == 11 :
			carte = "V"
		
		if carte == 12 :
			carte = "D"
		
		if carte == 13 :
			carte = "R"
		
		if carte == 14 :
			carte = "A"
		
		return carte

	#Fonction permettant l'affectation d'une carte dans la main d'un joueur
	#Via id_joueur et la fonction tirage_carte()
	def distribution(id_joueur ,deck) : 
		liste_joueurs[id_joueur].main.append(tirage_carte())
		liste_joueurs[id_joueur].main.append(tirage_carte())

	#Fonctions permettant de ne tirer qu'une seule carte
	#Pour les HIT de chaque joueur et le dealer	
	def tirage_unique(id_joueur):
		liste_joueurs[id_joueur].main.append(tirage_carte())

	#Fonction permettant l'affichage de la main du dealer, avec la deuxème carte cachée
	#Ou de tous les joueurs restants dans la parties en cours
	def aff_main(id_joueur, nbr_joueurs_r):
		
		if id_joueur == 0:
			print("\n\tMain du dealer : " + str(liste_joueurs[id_joueur].main[0]) + " | [Deuxième carte cachée]")
		
		else:
			
			for f in range(nbr_joueurs_r):
				print("Main " + str(liste_joueurs[f+1].name) + ": " + str(liste_joueurs[f+1].main).replace("'","") + "\t\t| TOTAL : " + str(total(liste_joueurs[f+1].main)))

	#Fonction permettant d'afficher toutes les cartes du dealer
	def aff_main_dealer_final():
		print("\n\tMain du dealer : " + str(liste_joueurs[0].main).replace("'","") + "\t\t| TOTAL : " + str(total(liste_joueurs[0].main)) + "\n\n")

	#Fonction permettant de connaitre le score total d'une main passée en parametre
	def total(main):
		result = 0
		
		for carte in main :
		
			if carte == "V" or carte == "D" or carte == "R":
				result = result + 10
			
			elif carte == "A":
				
				if result >= 11 :
					result = result + 1
				
				else :
					result = result + 11
			
			else :
				result = result + carte
				
		return result

	#Fonction permettant de détecter s'il y a BJ pour un joueur
	#Ainsi que le nombre de BJ dans la partie
	def scan_blackjack(nbr_joueurs):

		cpt_bj = 0

		changement_liste = 0

		for i in range(nbr_joueurs):
			if total(liste_joueurs[i+1].main) == 21:
			
				cpt_bj = cpt_bj + 1
			
				print("\nBravo " + str(liste_joueurs[i+1].name) + " ! Tu as un BLACKJACK, tu as gagné !")
				
				liste_joueurs[i+1].blackjack = 1
				
				changement_liste = 1

		return changement_liste, cpt_bj;

	#======================MAIN=======================

	def blackjack() :

		nbr_joueurs_r = nbr_joueurs
		
		a = 0
		
		print("\nNombre de joueurs : " + str(nbr_joueurs_r))

		#Distribution carte dealer
		distribution(0, deck)
		
		#Distribution cartes joueurs
		for i in range(nbr_joueurs):
			distribution(i+1, deck)

		print("\n\n\t\t================BLACKJACK================\n\n")

		aff_main(1, nbr_joueurs_r)

		#Recherche de BJ chez les joueurs
		tab_return = scan_blackjack(nbr_joueurs)
		
		changement_liste = tab_return[0]
		cpt = tab_return[1]
		
		#Dans le cas d'un ou plusieurs blackjack, affichage des joueurs encore en jeu
		while cpt != 0 :
		
			k = 0
			
			if changement_liste == 1:
				
				for u in range(nbr_joueurs_r):
					
					if liste_joueurs[u+1].blackjack == 1:
					
						print("\n\tRetrait du joueur vainqueur en cours : " + liste_joueurs[u+1].name + "\n\n")
					
						a = liste_joueurs.pop(u+1).name
						
						nbr_joueurs_r = nbr_joueurs_r - 1
						
						k = k + 1

					if k == 1 :
						break

				lib.load_bar(delay)
				
				clear()
				
				print("Nombre de joueurs restants : " + str(nbr_joueurs_r))
				
				print("\n\tListe des joueurs restants : ")
				
				print("\n\n\t\t================BLACKJACK================\n\n")
				
				aff_main(1, nbr_joueurs_r)
			
			cpt = cpt - 1

		#Affichage de la main du croupier
		aff_main(0, nbr_joueurs_r)
		
		for b in range(nbr_joueurs_r) :
		
			c = 1		
			
			while c != 0:
			
				choix = input("\n" + str(liste_joueurs[b+1].name) + " voulez vous tirer une carte ? [o/n] : ")
				
				clear()
				
				if choix == "o":
					
					tirage_unique(b+1)
					print("\n\n\t\t================BLACKJACK================\n\n")
					aff_main(1, nbr_joueurs_r)
					
				
				elif choix == "n":
					c = 0
					print("\n\n\t\t================BLACKJACK================\n\n")
					aff_main(1, nbr_joueurs_r)
					
					print("\n\n" + str(liste_joueurs[b+1].name) + ", Vous terminez la partie avec un score de " + str(total(liste_joueurs[b+1].main)))
					
					if b+1 < nbr_joueurs_r :
						print("\n\n\t\tJoueur suivant : " + str(liste_joueurs[b+2].name) + "\n\n")
					
					lib.load_bar(delay)
					
					c = 0
					
					clear()
					print("\n\n\t\t================BLACKJACK================\n\n")
					aff_main(1, nbr_joueurs_r)
				
				if total(liste_joueurs[b+1].main) > 21:
					print("\n\tScore : " + str(total(liste_joueurs[b+1].main)) + " \tVous avez perdu !")
					
					if b+1 < nbr_joueurs_r :
						print("\n\n\t\tJoueur suivant : " + str(liste_joueurs[b+2].name) + "\n\n")
					
					lib.load_bar(delay)
					c = 0
					
					clear()
					print("\n\n\t\t================BLACKJACK================\n\n")
					aff_main(1, nbr_joueurs_r)
					
				if total(liste_joueurs[b+1].main) == 21:
					print("\n\n\tBlackjack pour vous " + str(liste_joueurs[b+1].name) + "!\n\n")
					c = 0
					lib.load_bar(delay)

		return nbr_joueurs_r
		
	#Fonction effectuant le tirage du dealer a la fin de la partie
	#Avant le calcul des scores 
	def tirage_dealer(nbr_joueurs_r):
	
		defaite_dealer = 0
		
		clear()
		
		print("\n\n\t\t================BLACKJACK================")
		
		while total(liste_joueurs[0].main) < 16:
			
			tirage_unique(0)
		
		aff_main_dealer_final()
		
		if total(liste_joueurs[0].main) > 21:
			
			print("\n\n\tLa Banque saute, défaite de la maison !\n\n")
			
			print("\n\n\tTous les joueurs restants gagnent")
			
			exit()
			
		elif total(liste_joueurs[0].main) == 21:
			
			print("\n\n\tLa Banque gagne par BLACKJACK, défaites des joueurs en dessous 21 !\n\n")
			
			defaite_dealer = 1
			
		return defaite_dealer

	def gestion_score_final(nbr_joueurs_r, defaite_dealer):

		perdant = []
		
		print("\n\tAffichage des scores dans 5 secondes ... \n\n")
		
		lib.load_bar(5)
		
		clear()
		
		print("\n\n\t\t================BLACKJACK================")
		print("\n\t\t==================SCORE==================\n\n")
		
		aff_main_dealer_final()
		aff_main(1, nbr_joueurs_r)
		
		for z in range(nbr_joueurs_r):
			
			if total(liste_joueurs[0].main) > total(liste_joueurs[z+1].main) or total(liste_joueurs[z+1].main) > 21:
				
				print("\n\t" + liste_joueurs[z+1].name + " a perdu")
				
				perdant.append(z+1)
				
			elif total(liste_joueurs[0].main) < total(liste_joueurs[z+1].main) :
				
				print("\n\t" + liste_joueurs[z+1].name + " a gagné")
				
				if total(liste_joueurs[z+1].main) == 21:
				
					print("\n\t" + liste_joueurs[z+1].name + " a Obtenu un Blackjack, double mise")
			
			elif total(liste_joueurs[0].main) == total(liste_joueurs[z+1].main):
				
				print("\n\t" + liste_joueurs[z+1].name + " récupère sa mise ")

		for m in range(len(perdant)):
		
			liste_joueurs.pop(perdant[m])


	players_base = blackjack()

	dealer_def = tirage_dealer(players_base)

	gestion_score_final(players_base, dealer_def)
	
#======================STARTUP=======================
while True :
	jeu()
