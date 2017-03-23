#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-

""" Fichier comportant le programme Decode_Cesar permettant de décoder n'importe quel texte crypté par le code de César.
	Pour ce faire, chaque pas de 0 à 25 est testé dans l'ordre décroissant et le résultat du décodage par la fonction decode_cesar_v2 est affiché.
	Si le texte est cohérent, l'utilisateur saisit 'o' pour oui et le programme s'arrête.
	Sinon, il saisit 'n' pour non et le programme passe au pas suivant.
	Les pas sont testés dans l'ordre décroissant, en commençant par n=25.
"""

import os									# Importation des fonctions nécessaires à l'execution du code.
from fonctions.decode_cesar_v2 import *						# Dont la fonction decode_cesar1 présente dans le fichier du même nom	
f_exp = open ("cesar_cryp.txt","r")						# Fonction permettant l'exportation du texte crypté contenu dans le fichier cesar_cryp.txt
f_imp = open ("cesar_decryp.txt","w")						# Fonction permettant l'importation du texte décrypté dans le fichier cesar_décryp.txt
c=f_exp.read()									# Variable qui contient le texte crypté.
n=25										# Variable contenant le pas, égal à 25 au départ.
b=str()										# Variable qui contiendra le texte décrypté.
i=str()										# Variable permettant d'intéragir avec l'utilisateur.
titre=str("Bienvenue dans le programme Decode_Cesar !")				# Présentations du programme.
print("", titre.upper().center(75),"\n")
print("Dans ce programme, chaque pas est testé.")
print("Il est demandé à l'utilisateur d'attester de la cohérence du texte décodé pour chaque pas.")
print("En cas de non cohérence, le pas suivant est testé, dans l'ordre décroissant.")
print("Le premier test étant effectué avec un pas égal à 25")
print("La casse est préservé.")
print("Une MAJUSCULE renvoie une MAJUSCULE, et une minuscule renvoie une minuscule.")
print("Les caractères autres qu'alphabétique sont préservés.\n")
input("Appuyez sur n'importe quelle touche pour lancer le décryptage...\n")
				
while n!=0 and i.lower()!="o":							# Tant que tout les pas n'ont pas été testé,
	print("\nTentative de décryptage avec un pas n =",n,"\n")		# Ou que l'utilisateur n'atteste pas de la cohérence du texte testé au pas actuel,
	b=decode_cesar1(c, n)							# La boucle continue de tourner.
	print(b)
	print("\nLe texte est-il cohérent ?")
	i=input("Saisissez 'o' pour oui, 'n' pour non.\n")
	n-=1																			
	
if n!=0 :									# Si la boucle s'est arrêtée avant que n n'arrive à 0,
	print("\nLe pas de décalage était de", n+1, "\n")			# C'est que l'utilisateur à attesté de la cohérence d'un texte décrypté pour un certain pas.
	print("Le texte décodé est donc :")
	print(b)								# On affiche alors le texte décrypté.
	
else :										# Sinon, la boucle s'arrête lorsque n=0, donc le texte codé ne l'était pas en César.
	print("\nLe texte proposé au lancement du programme n'était pas en code César.\n")
	print(c)
	
f_imp.write(b)
f_exp.close()
f_imp.close()
print("\nLe texté décrypté à été enregistré dans le fichier cesar_decryp.txt !")

input("\nTapez n'importe quel caractère pour fermer le programme...\n")		# Permet au programme de s'executer dans la console et d'être lisible par l'utilisateur.
										 
