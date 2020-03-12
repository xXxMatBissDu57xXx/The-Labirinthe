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
      joueurs.append(Joueur(i))
    return joueurs

def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs.append(Joueur(joueur))
    #print("Joueurs après ajouterJoueur :\n",joueurs)

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    indiceCourant=random.randint(0,len(joueurs)-1)
    listeBis=joueurs
    joueurs=[]
    joueurs.append(listeBis[indiceCourant])
    joueurs[0]["numero"]=0
    listeBis.pop(indiceCourant)
    for i in range(len(listeBis)):
      joueurs.append(listeBis[i])
      joueurs[i+1]["numero"]=i+1
      #print("joueurs :",joueurs)

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
        ajouterTresor(joueurs[i],tresor)
        Tresors.remove(tresor)
        i +=1
        if i ==len(joueurs)-1:
          i =-1
    else:
      i=0
      while len(joueurs[len(joueurs)-1]["tresors"]) <nbTresorMax:
        tresor=random.choice(Tresors)
        ajouterTresor(joueurs[i],tresor)
        Tresors.remove(tresor)
        i +=1
        if i ==len(joueurs)-1:
          i =-1
    #print(joueurs)

def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """  
    for i in range(len(joueurs)):
      if joueurs[i]["numero"] >0:
        joueurs[i]["numero"] -=1
      else: 
        joueurs[i]["numero"] =len(joueurs)-1
    #print("joueurs après changement de joueur courant :\n",joueurs)

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
    for i in range(len(joueurs)):
      if joueurs[i]["numero"] ==0:
        return joueurs[i]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    for i in range(len(joueurs)):
      if joueurs[i]["numero"] ==0:
        tresorTrouve(joueurs[i])
    #print(joueurs)

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
    for i in range(len(joueurs)):
      if joueurs[i]["numero"] ==0:
        return i

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    for i in range(len(joueurs)):
      if joueurs[i]["numero"] ==0:
        return getNom(joueurs[i])

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
    return prochainTresor(joueurs[numJoueur])
    
def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    for i in range(len(joueurs)):
      if joueurs[i]["numero"] ==0:
        return prochainTresor(joueurs[i])

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    for i in range(len(joueurs)):
      if joueurs[i]["numero"] ==0:
        if len(joueurs[i]["tresors"]) ==0:
          return True
    return False


if __name__=="__main__":
  liste=["Mat","Dams","Gui","JoJo"]
  liste2=[{"nom":"Mat","tresors":[5,6],"numero":1},{"nom":"Dams","tresors":[9,8],"numero":0}]
  #print("ListeJoueurs :",ListeJoueurs(liste))
  #ajouterJoueur(liste,"Gui")
  #initAleatoireJoueurCourant(ListeJoueurs(liste))
  #distribuerTresors(liste2,nbTresors=24, nbTresorMax=0)
  #changerJoueurCourant(liste2)
  #print(getNbJoueurs(liste))
  #print(getJoueurCourant(liste2))
  #joueurCourantTrouveTresor(liste2)
  #print(nbTresorsRestantsJoueur(liste2,1))
  #print(numJoueurCourant(liste2))
  #print(nomJoueurCourant(liste2))
  #print(nomJoueur(liste2,1))
  #print(prochainTresorJoueur(liste2,0))
  #print(tresorCourant(liste2))
  #print(joueurCourantAFini(liste2))
  