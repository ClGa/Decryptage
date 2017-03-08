# -*- coding:utf-8 -*-
""" Ce fichier contient la v1 de la fonction decode_cesar1 qui décrypte un texte codé avec l'algorithme de César pour un décalage prédéfini.
Par défaut, elle renvoie la chaine de caractère avec une décalage égal à 0 """

def decode_cesar1(c, n=0): # La fonction prend en paramètre une chaîne de caractère c et un nombre n correspondant au décalage du cryptage.
	l = len(c) # On associe une variable à la longueur de c
	cDecrypt = "" # Variable qui contiendra le message décrypté
	a=0 # Variable qui contiendra le code ascii des caractères de c et cDecrypt
	for i in range(l) : # Boucle permettant de parcourir chaque caractère de c
		if ord(c[i]) < 65 or (ord(c[i]) > 90 and ord(c[i]) < 97) or ord(c[i]) > 122 :  # La fonction ord permet de récupérer le code ascii du i ème caractère de c
			a=ord(c[i]) # On affecte à la variable a le code ASCII du i ème caractère de c
			cDecrypt+=chr(a) # La fonction chr permet d'ajouter à cDecrypt le caractère correspondant au code contenu dans a	
			# Si le code ASCII du i ème caractère de c est différent de celui d'une lettre MAJUSCULE ou minuscule
			# Aucun décalage n'est effectué et on ajoute à cDecrypt le même caractère
		elif ord(c[i]) >= 65 and ord(c[i]) <= 90 : # Si le ième caractère de c est une lettre MAJUSCULE
			a=ord(c[i])+n # On affecte à a le code ASCII du ième caractère de c et on lui ajoute le décalage
			if a < 65 : # En cas de pas négatif, le nombre affecté à a peut-être sortir du champs des lettres MAJUSCULE
				cDecrypt+=chr(a+26) # On lui ajoute alors 26 pour affecter à cDecrypt la lettre désirée
			elif a > 90 : # Si le nombre affecté à a sort du champs des lettres MAJUSCULE
				cDecrypt+=chr(a-26) # On lui soustrait alors 26 pour affecter à cDecrypt la lettre désirée
			else : # Si le nombre affecté à a reste dans le champs des lettres MAJUSCULE
				cDecrypt+=chr(a) # On affecte à cDecrypt le caractère correspondant
		else : # Si le ième caractère de c est une lettre minuscule, on procède de la même façon qu'au dessus
			a=ord(c[i])+n 
			if a < 97 :
				cDecrypt+=chr(a+26)
			elif a > 122 :
				cDecrypt+=chr(a-26)
			else :
				cDecrypt+=chr(a)
	return cDecrypt # La fonction retourne la chaîne décryptée