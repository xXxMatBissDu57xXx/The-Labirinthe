# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""

from matrice import *
from carte import *

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """

    cartes = creerCartesAmovibles(1, nbTresors)

    #PLACER LES CARTES
    plateau = Matrice(7,7, None)
    for ligne in range(7) :
        for case in range(7) :
            plateau[ligne][case] = cartes[-1]
            cartes.pop()

    #PLACER LES JOUEURS
    poserPionPlateau(plateau, 0, 0, 1)
    if nbJoueurs>1:
        poserPionPlateau(plateau, 6, 6, 2)
        if nbJoueurs>2:
            poserPionPlateau(plateau, 0, 6, 3)
            if nbJoueurs >3:
                poserPionPlateau(plateau, 6, 0, 4)


    return (plateau,cartes[0])

def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    cartes = []
    tresors = list(range(1, nbTresors+1))

    for i in range(50) :
        cartes.append(Carte(True, True, True, True))
        cartes[i]["pions"] = []
        while not estValide( cartes[-1] ) :
            decoderMurs(cartes[-1], random.randint(0, 15))
        if tresors :
            cartes[i]["tresor"] = tresors.pop()
            
    random.shuffle(cartes)

    return cartes

def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """

    if plateau[lig][col]["tresor"] == numTresor :
        plateau[lig][col]["tresor"] = 0
        return True
    return False

    return

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """

    for ligne in range(7):
        for case in range(7):
            if plateau[ligne][case]["tresor"] == numTresor :
                return (ligne,case)
    else : 
        return None

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """

    for ligne in list(range(7)):
        for case in list(range(7)):
            if numJoueur in plateau[ligne][case]["pions"]:
                return (ligne,case)
    else : 
        return None
    
def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """

    if numJoueur in plateau[lin][col]["pions"] :
        plateau[lin][col]["pions"].remove(numJoueur)
        return True
    return False

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    pions = getListePions(plateau[lin][col])
    if numJoueur not in pions :
        pions.append(numJoueur)
        plateau[lin][col]["pions"] = pions

def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    pass

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass

if __name__=='__main__':

    # 9 FONCTIONS
    nbJoueurs = 2
    nbTresors = 8
    plateau,carte = Plateau(nbJoueurs,nbTresors)
    cartes = creerCartesAmovibles(1, nbTresors)

    tmp = 0
    for carte in cartes :
        if carte["tresor"]:
            tmp += 1
    assert tmp == nbTresors, "Plateau"

    assert len(cartes) == 50, "creerCartesAmovibles"
    for carte in cartes :
        assert estValide(carte), "creerCartesAmovibles"

    plateau[0][0]["tresor"] = 100
    assert prendreTresorPlateau(plateau, 0, 0, 100), "prendreTresorPlateau"
    assert not prendreTresorPlateau(plateau, 0, 0, 100), "prendreTresorPlateau"

    plateau[5][5]["tresor"] = 100
    assert getCoordonneesTresor(plateau, 100) == (5, 5), "getCoordonneesTresor"


    plateau[5][5]["pions"] = [5]
    assert getCoordonneesJoueur(plateau, 5) == (5,5), "getCoordonneesJoueur"

    assert prendrePionPlateau(plateau, 5, 5, 5), "prendrePionPlateau"
    assert not prendrePionPlateau(plateau, 5, 5, 5), "prendrePionPlateau"

    poserPionPlateau(plateau, 2, 2, 3)
    assert getCoordonneesJoueur(plateau, 3) ==(2,2), "poserPionsPlateau"