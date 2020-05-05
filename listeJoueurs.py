# -*- coding: utf-8 -*-
""" 
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    listeJoueurs = {"indiceCourant": 0, "joueurs": []}
    for i in nomsJoueurs:
      listeJoueurs["joueurs"].append(Joueur(i))
    return listeJoueurs

def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs["joueurs"].append(joueur)

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs["indiceCourant"] = random.randint(0, len(joueurs["joueurs"])-1)

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    if nbTresors == 0:
        nbTresors = 48
    tresors = list(range(nbTresors))
    while tresors:
        for joueur in joueurs["joueurs"] :
            tresor=random.choice(tresors)
            ajouterTresor(joueur,tresor)
            tresors.remove(tresor)

def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """  
    if joueurs["indiceCourant"] < len(joueurs["joueurs"])-1:
        joueurs["indiceCourant"] += 1  
    else:
        joueurs["indiceCourant"] = 0

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs["joueurs"])

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs["joueurs"][joueurs["indiceCourant"]]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """

    tresorTrouve(joueurs["joueurs"][joueurs["indiceCourant"]])

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    return getNbTresorsRestants(joueurs["joueurs"][numJoueur-1])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs["indiceCourant"]+1

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return getNom(joueurs["joueurs"][joueurs["indiceCourant"]])

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return getNom(joueurs["joueurs"][numJoueur-1])

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    return prochainTresor(joueurs["joueurs"][numJoueur])
    
def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return prochainTresor(joueurs["joueurs"][joueurs["indiceCourant"]])

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """

    return not bool(joueurs["joueurs"][joueurs["indiceCourant"]]["tresors"])


if __name__=="__main__":

    liste = ListeJoueurs(["Mat","Dams","Gui"])

    joueur = Joueur("Jojo")

    assert len(liste["joueurs"]) == 3, "ListeJoueurs()"
    assert liste["indiceCourant"] == 0, "ListeJoueurs()"

    ajouterJoueur(liste, joueur)
    assert len(liste["joueurs"]) == 4, "ajouterJoueur()"

    initAleatoireJoueurCourant(liste)
    assert liste["indiceCourant"] in list(range(4)), liste["indiceCourant"] #""""initAleatoireJoueurCourant()""""

    distribuerTresors(liste)
    for joueur in liste["joueurs"] :
        assert len(joueur["tresors"]) == 6, "distribuerTresors()"

    liste["indiceCourant"] = 2
    changerJoueurCourant(liste)
    assert liste["indiceCourant"] == 3, "changerJoueurCourant()"
    changerJoueurCourant(liste)
    assert liste["indiceCourant"] == 0, "changerJoueurCourant()"
    
    assert getNbJoueurs(liste) == 4, "getNbJoueurs()"

    assert getJoueurCourant(liste)["nom"] == "Mat", "getJoueurCourant"

    joueurCourantTrouveTresor(liste)
    assert len(getJoueurCourant(liste)["tresors"]) == 5, "joueurCourantTrouveTresor"

    assert nbTresorsRestantsJoueur(liste, 1) == 5, "nbTresorsRestantsJoueur"
    
    assert numJoueurCourant(liste) == 1, "numJoueurCourant"

    assert nomJoueurCourant(liste) == "Mat", "nomJoueurCourant"

    assert nomJoueur(liste, 1) == "Mat", "nomJoueur"
    
    assert prochainTresorJoueur(liste, 0) == liste["joueurs"][0]["tresors"][-1], "prochainTresorJoueur"

    assert tresorCourant(liste) == liste["joueurs"][0]["tresors"][-1], "tresorCourant"

    assert not joueurCourantAFini(liste), "joueurCourantAFini"
    while bool(prochainTresorJoueur(liste, 0)):
        tresorTrouve(getJoueurCourant(liste))

    assert joueurCourantAFini(liste), 'joueurCourantAFini'