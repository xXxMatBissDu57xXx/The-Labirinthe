# -*- coding: utf-8 -*-
"""
        Projet Labyrinthe 
        Projet Python 2020 - Licence Informatique UNC (S3 TREC7)
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""

import random

"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']

#carte(codeMurs,numTresor,codeJoueurs)


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """

	"""
	carte = [int([bin(nord==True)],[bin(est==True)],[bin(sud==True)],[bin(ouest==True)]), tresor, 0]
	for(i in pions):
		poserPion(carte, i)
	return carte
	"""

	carte = {"nord":nord,"est":est,"sud":sud,"ouest":ouest,"tresor":tresor,"pions":pions}
	return carte
    pass

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
	"""
	if bin(c).count(1) < 3:
		return True 
	else :
		return False
	"""
	if([c.get(nord),c.get[est],c.get[sud],c.get(ouest)].count(1)<3):
		return True
	else:
		return False  

	pass

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
	if(c.get(nord)==True):
		return True
	else:
		return False
    pass

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
	if(c.get(sud)==True):
		return True
	else:
		return False
    pass

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
	if(c.get(est)===True):
		return True
	else:
		return False
    pass

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
	if(c.get(ouest)==True):
		return True
	else:
		return False
    pass

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
	"""
	listePions = []
	if (bin(c[2]).count(1) > 1):
		for(i = 0; len < bin(c).count(1); i ++): 
			if c[i] == 1:
				listePions.append(2**i)
    return listePions
	"""

	return c.get("pions")

	pass

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """

	"""
	for i in listePions:
		c[i-1] = 1
	"""

	c["pions"] = listePions

	pass

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """

	"""
	return(bin(c[2]).count(1))
	"""

	nbPions = 0
	for i in getListePions(c):
		nbPions += 1
	return nbPions

    pass

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
	"""
	if(bin(c)[pion-1] == 1):
		return True
	else:
		return False
	"""

	for i in c.get("pions"):
		if i == pion :
			return True
	return False
    pass


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
	"""
	return c[1];
	"""

	return c.get("tresor")
    pass

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
	"""
	tmp = getTresor(c)
	c[1] = 0
	return tmp
	"""

	tresor = getTresor(c)
	c["tresor"] = 0
	return tresor

    pass

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
	"""
	tmp = getTresor(c)
	c[1] = tresor
	return tmp
	"""

	tmp = c.get("tresor")
	c["tresor"]=tresor


    pass

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
	"""
	tmp = bin(c[2])
		tmp[pion-1] = 0
	c[2] = int(tmp, 2)
	"""
	if possedePion(c, pion):
			c["pions"].remove(i)

    pass

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
	"""
	if(bin(c[2])[pion-1] == 1):
		tmp = bin(c[2])
		tmp[pion-1] = 0
		c[2] = int(tmp, 2)
	else:
	"""
    if not possedePion(c,pion):
		c["pions"].append(pion)

	pass

def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
	"""
	tmp = bin(c[2])
	tmp.append(tmp[0])
	tmp.pop(0)
	c[2] = int(tmp, 2)
	"""
	tmp = c["nord"]
	c["nord"] = c["ouest"]
	c["ouest"] = c["sud"]
	c["sud"] = c["est"]
	c["est"] = c["tmp"]


    pass

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
	"""
	tmp = bin(c[2])
	tmp.reverse()
	tmp.append(tmp[0])
	tmp.pop(0)
	tmp.reverse
	c[2] = int(tmp, 2)
	"""
	tmp = c["nord"]
	c["nord"] = c["est"]
	c["est"] = c["sud"]
	c["sud"] = c["ouest"]
	c["ouest"] = c["tmp"]
    pass

def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
	for(i=1, i<randint(0,3),i++)
		tournerHoraire(c)

    pass

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
	"""
	return c[0]
	"""
	return int([bin(nord)],[bin(est)],[bin(sud)],[bin(ouest)],2)

    pass

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """    
	c["nord"] = bool(bin(code)[0])
	c["est"] = bool(bin(code)[1])
	c["sud"] = bool(bin(code)[2])
	c["ouest"] = bool(bin(code)[3])

    pass


def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
	return listeCartes[coderMurs]
    pass

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """

	if((carte1["nord"] == True)and(carte1["sud"] == True)):
		return True
	else : 
		return false
    pass

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """

	if((carte1["sud"] == True)and(carte1["nord"] == True)):
		return True
	else : 
		return false
    pass

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """

	if((carte1["ouest"] == True)and(carte1["est"] == True)):
		return True
	else : 
		return false
    pass

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """

	if((carte1["est"] == True)and(carte1["ouest"] == True)):
		return True
	else : 
		return false
    pass

if __name__=='__main__':
	c1 = Carte(1,1,1,1)