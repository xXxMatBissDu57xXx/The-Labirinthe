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
    joueurs["joueurs"].append(Joueur(joueur))
    #print("Joueurs après ajouterJoueur :\n",joueurs)

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    """indiceCourant=random.randint(0,len(joueurs)-1)
    listeBis=joueurs
    joueurs=[]
    joueurs.append(listeBis[indiceCourant])
    joueurs[0]["numero"]=0
    listeBis.pop(indiceCourant)
    for i in range(len(listeBis)):
      joueurs.append(listeBis[i])
      joueurs[i+1]["numero"]=i+1
    """
    joueurs["indiceCourant"] = random.randint(0, len(joueurs["joueurs"])-1)

    print("Liste des joueurs à la fin de initAleatoireJoueurCourant :",joueurs)

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
    Tresors=[]
    for i in range(nbTresors):
      Tresors.append(i+1)
    if nbTresorMax ==0:
      i=0
      while len(Tresors) !=0:
        tresor=random.choice(Tresors)
        ajouterTresor(joueurs["joueurs"][joueurs["indiceCourant"]],tresor)
        Tresors.remove(tresor)
        i +=1
        if i ==len(joueurs["joueurs"])-1:
          i =-1
    else:
      i=0
      while len(joueurs["joueurs"][len(joueurs["joueurs"])-1]["tresors"]) <nbTresorMax:
        tresor=random.choice(Tresors)
        ajouterTresor(joueurs["joueurs"][i],tresor)
        Tresors.remove(tresor)
        i +=1
        if i ==len(joueurs["joueurs"])-1:
          i =-1
    #print(joueurs)

def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """  
    if joueurs["indiceCourant"] < len(joueurs["joueurs"]):
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
    return joueurs["indiceCourant"]

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

    return bool(joueurs["joueurs"][joueurs["indiceCourant"]]["tresors"])


if __name__=="__main__":
  liste=["Mat","Dams","Gui","JoJo"]
  joueurs2={"indiceCourant":0,"joueurs":[{"nom":"Mat","tresors":[]},{"nom":"Dams","tresors":[]}]}
  joueurs = ListeJoueurs(liste)
  print("ListeJoueurs :",ListeJoueurs(joueurs))
  ajouterJoueur(joueurs,"Gui")
  initAleatoireJoueurCourant(joueurs)
  distribuerTresors(joueurs2,nbTresors=24, nbTresorMax=0)
  changerJoueurCourant(joueurs2)
  print(getNbJoueurs(joueurs))
  print(getJoueurCourant(joueurs2))
  joueurCourantTrouveTresor(joueurs2)
  print(nbTresorsRestantsJoueur(joueurs2,1))
  print(numJoueurCourant(joueurs2))
  print(nomJoueurCourant(joueurs2))
  print(nomJoueur(joueurs2,1))
  print(prochainTresorJoueur(joueurs2,0))
  print(tresorCourant(joueurs2))
  print(joueurCourantAFini(joueurs2))
  