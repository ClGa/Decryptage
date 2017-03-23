# -*- coding:utf-8 -*-
""" 
Ce fichier contient la v2 de la fonction decode_cesar1 qui décrypte un texte codé avec l'algorithme de César pour un décalage prédéfini par l'utilisateur.
Par défaut, elle renvoie la chaine de caractère avec un décalage égal à 0, c'est à dire elle même
Différences par rapport à la v1 :
		.Les pas non inclus dans [0,25] sont ramenés à leur équivalent sur cet intervalle.
		.Fusion des boucles MAJUSCULE et minuscule en une seule.
		.Ajout de la variable "o" pour plus de lisibilité.
		.Commentaire décalé par rapport au code pour plus de lisibilité.
		.Ajout d'espaces divers pour plus de lisibilité.
"""

import string
import os

def decode_cesar1(c, n=0) :							    # La fonction prend en paramètre une chaîne de caractère c et un nombre n correspondant au décalage du cryptage.
	l = len(c) 								    # On associe une variable à la longueur de c.
	cDecrypt = "" 								    # Chaine de caractère vide qui contiendra le message décrypté.
	i=0									    # Variable permettant le parcours de la chaine de caractère.
	a=0 									    # Variable qui contiendra le code ascii des caractères à affecter à cDecrypt.
	o=0									    # Variable qui contiendra le code ascii de chaque ième caractère de c.										
	while abs(n) >= 26 or (abs(n) < 26 and n < 0): 
										    # Boucle permettant de ramener un pas non inclus entre 0 et 25 à son équivalent sur cet intervalle.
		if n < 0 : 							    # Par exemple : n=27 équivaut à n=1 et n=-2 équivaut à n=24.
			n += 26
		else :
			n -= 26
	for i in range(l) : 							      # Boucle permettant de parcourir chaque caractère de c.
		o = ord(c[i]) 							      # La fonction ord permet de récupérer le code ASCII du i ème caractère de c dans la variable o.
		if c[i] in string.ascii_lowercase or c[i] in string.ascii_uppercase : # Si la ieme lettre de c est une MAJ ou une min
			a = o + n 						      # On affecte à a le code ASCII du ième caractère de c et on lui ajoute le décalage n.
			if a > 122 or o < 91 and a > 90  :  			      # Si le nombre affecté à a sort du champs des lettres minuscule,
										      # ou s'il sort du champs des lettres MAJUSCULE alors que o codait une MAJUSCULE,
				cDecrypt += chr(a-26) 				      # On lui soustrait alors 26 pour affecter à cDecrypt la lettre décodée.
			else : 							      # Si le nombre affecté à a reste dans le champs des lettres MAJUSCULE ou minuscule,
				cDecrypt += chr(a) 				      # On affecte à cDecrypt le caractère correspondant et décodé.
										      # La fonction chr permet d'ajouter à cDecrypt le caractère correspondant au code contenu dans o.
		else : 								      # Si le ième caractère de c n'est ni une lettre MAJUSCULE, ni minuscule,
			cDecrypt+=chr(o)					      # On affecte à cDecrypt le même caractère
	return cDecrypt 							      # La fonction retourne la chaîne décryptée.

if __name__ == "__main__":	# Permet de tester le bon fonctionnement de la fonction decode_cesar1 directement en executant le fichier .py
	c="cZz 1 ?"
	print("", decode_cesar1(c, 1))
	print("Si la fonction s'execute correctement, elle doit afficher 'dAa 1 ?'")
	input("Tapez n'importe quel caractère pour fermer la fenêtre...")
