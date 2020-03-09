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
    joueurs=[]
    for i in nomsJoueurs:
      joueurs.append((i,[]))
    return joueurs

def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs.append(joueur)

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    indiceCourant=random.randint(0,len(joueurs[0])-1)
    listeBis=joueurs
    joueurs=[]
    joueurs.append((listeBis[indiceCourant],[0]))
    listeBis.pop(indiceCourant)
    j=1
    for i in listeBis:
      joueurs.append((i,[j]))
      j +=1

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
        joueurs[i][0][1].append(tresor)
        Tresors.remove(tresor)
        i +=1
        if i ==len(joueurs)-1:
          i =-1
    else:
      i=0
      while len(joueurs[len(joueurs)-1][0][1]) <nbTresorMax:
        tresor=random.choice(Tresors)
        joueurs[i][0][1].append(tresor)
        Tresors.remove(tresor)
        i +=1
        if i ==len(joueurs)-1:
          i =-1

def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """ 
    j=0  
    for i in joueurs:
      if joueurs[j][1][0] >0:
        joueurs[j][1][0] -=1
      else: 
        joueurs[j][1][0] =len(joueurs)-1
      j +=1

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs)

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    for i in range(len(joueurs)-1):
      if joueurs[i][1][0] ==0:
        return joueurs[i]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    for i in range(len(joueurs)-1):
      if joueurs[i][1][0] ==0:
        joueurs[i][0][1].pop(0)

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    return getNbTresorsRestants(joueurs[numJoueur])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    for i in range(len(joueurs)-1):
      if joueurs[i][1][0] ==0:
        return i

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    for i in range(len(joueurs)-1):
      if joueurs[i][1][0] ==0:
        return joueurs[i][0][0]

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return getNom(joueurs[numJoueur])

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    return joueurs[numJoueur][0][1][0]

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    for i in range(len(joueurs)-1):
      if joueurs[i][1][0] ==0:
        return joueurs[i][0][1][0]

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    for i in range(len(joueurs)-1):
      if joueurs[i][1][0] ==0:
        if len(joueurs[i][0][1]) ==0:
          return True
    return False


if __name__=="__main__":
  liste=[(("Mat"),[]),(("Dams"),[])]
  print(ListeJoueurs(liste))
  ajouterJoueur(liste,(("Gui"),[]))
  ajouterJoueur(liste,(("Briane"),[]))
  print(ListeJoueurs(liste))
  initAleatoireJoueurCourant(liste)
  print(liste)
  print(changerJoueurCourant(liste))
  