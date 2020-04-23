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

    plateau={"matrice": Matrice(7,7, None), "carte": cartes.pop()}

    #PLACER LES CARTES STABLES
    setVal(getMatrice(plateau),0,0,Carte(True,False,False,True))
    setVal(getMatrice(plateau),0,2,Carte(True,False,False,False))
    setVal(getMatrice(plateau),0,4,Carte(True,False,False,False))
    setVal(getMatrice(plateau),0,6,Carte(True,True,False,False))

    setVal(getMatrice(plateau),2,0,Carte(False,False,False,True))
    setVal(getMatrice(plateau),2,2,Carte(False,False,False,True))
    setVal(getMatrice(plateau),2,4,Carte(True,False,False,False))
    setVal(getMatrice(plateau),2,6,Carte(False,True,False,False))

    setVal(getMatrice(plateau),4,0,Carte(False,False,False,True))
    setVal(getMatrice(plateau),4,2,Carte(False,False,True,False))
    setVal(getMatrice(plateau),4,4,Carte(False,True,False,False))
    setVal(getMatrice(plateau),4,6,Carte(False,True,False,False))

    setVal(getMatrice(plateau),6,0,Carte(False,False,True,True))
    setVal(getMatrice(plateau),6,2,Carte(False,False,True,False))
    setVal(getMatrice(plateau),6,4,Carte(False,False,True,False))
    setVal(getMatrice(plateau),6,6,Carte(False,True,True,False))

    #PLACER LES CARTES AMOVIBLES
    for ligne in range(7) :
        for case in range(7) :
            if not getMatrice(plateau)[ligne][case]:
                setVal(getMatrice(plateau),ligne,case,cartes[-1])
                cartes.pop()

    #PLACER LES JOUEURS
    poserPionPlateau(getMatrice(plateau), 0, 0, 1)
    if nbJoueurs>1:
        poserPionPlateau(getMatrice(plateau), 6, 6, 2)
        if nbJoueurs>2:
            poserPionPlateau(getMatrice(plateau), 0, 6, 3)
            if nbJoueurs >3:
                poserPionPlateau(getMatrice(plateau), 6, 0, 4)

    return (plateau)

def getMatrice(plateau):
    return plateau["matrice"]

def getCarte(plateau):
    return plateau["carte"]

def changerCarte(plateau, carte):
    plateau["carte"] = carte

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

     
    #20 COINS MOINS 4 PLACES DE BASE
    for i in range(16):
        cartes.append(Carte(False, False, True, True))

    #18 T MOINS 12 PLACES DE BASE
    for i in range(6):
        cartes.append(Carte(False, False, False, True))

    #DOUZE COULOIRS
    for i in range(12):
        cartes.append(Carte(False, True, False, True))

    random.shuffle(cartes)

    for carte in cartes :
        if tresors :
            mettreTresor(carte, tresors.pop())

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

    if numTresor == getTresor(plateau[lig][col]):
        prendreTresor(plateau[lig][col])
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
            if numTresor == getTresor(plateau[ligne][case]):
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
            if numJoueur in getListePions(plateau[ligne][case]):
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
    prendrePion(plateau[lin][col], numJoueur)

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    poserPion(plateau[lin][col], numJoueur)

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
    explorateur = Matrice(7, 7, False)
    action = True

    explorateur[ligD][colD] = True
    
    while action and explorateur[ligA][colA] == False:
        action = False
        for i in range(1, 50):
            for ligne in range(7):
                for case in range(7):
                    if explorateur[ligne][case] == i:
                        if ligne-1 > 0 and not explorateur[ligne-1][case]  and passageNord(plateau[ligne][case], plateau[ligne-1][case]) :
                            explorateur[ligne-1][case] = True
                            action = True
                        if  case+1 < 6 and not explorateur[ligne][case+1] and passageEst(plateau[ligne][case], plateau[ligne][case+1]):
                            explorateur[ligne][case+1] = True
                            action = True
                        if  ligne+1 < 6 and not explorateur[ligne+1][case] and passageSud(plateau[ligne][case], plateau[ligne+1][case]):
                            explorateur[ligne+1][case] = True
                            action = True
                        if  case-1 > 0 and not explorateur[ligne][case-1] and passageOuest(plateau[ligne][case], plateau[ligne][case-1]):
                            explorateur[ligne][case-1] = True
                            action = True
            if not action :
                break
    return explorateur[ligA][colA]


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
    explorateur = Matrice(7, 7, None)
    action = True

    for ligne in range(7):
        for case in range(7):
            explorateur[ligne][case] = []
    explorateur[ligD][colD] = [(ligD, colD)]
    
    while action and explorateur[ligA][colA] == []:
        action = False
        for i in range(1, 50):
            for ligne in range(7):
                for case in range(7):
                    if len(explorateur[ligne][case]) == i:
                        if  ligne > 0 and explorateur[ligne-1][case] == [] and passageNord(plateau[ligne][case], plateau[ligne-1][case]) :
                            explorateur[ligne-1][case] = explorateur[ligne][case].copy()
                            explorateur[ligne-1][case].append((ligne, case))
                            action = True
                        if  case < 6 and explorateur[ligne][case+1] == [] and passageEst(plateau[ligne][case], plateau[ligne][case+1]):
                            explorateur[ligne][case+1] = explorateur[ligne][case].copy()
                            explorateur[ligne][case+1].append((ligne, case))
                            action = True
                        if  ligne < 6 and explorateur[ligne+1][case] == [] and passageSud(plateau[ligne][case], plateau[ligne+1][case]):
                            explorateur[ligne+1][case] = explorateur[ligne][case].copy()
                            explorateur[ligne+1][case].append((ligne, case))
                            action = True
                        if  case > 0 and explorateur[ligne][case-1] == [] and passageOuest(plateau[ligne][case], plateau[ligne][case-1]):
                            explorateur[ligne][case-1] = explorateur[ligne][case].copy()
                            explorateur[ligne][case-1].append((ligne, case))
                            action = True
            if not action :
                break

    #AFFICHAGE ?
    if False :
        for ligne in explorateur:
            for case in ligne :
                print("[", end = ' ')
                for i in range(len(case)):
                    print(case[i], end = ' ')
                print("]", end = ' ')
            else :
                print(" ")
        print(explorateur[ligA][colA])

    if explorateur[ligA][colA]:
        explorateur[ligA][colA].pop(0)
        explorateur[ligA][colA].append((ligA,colA))
        return explorateur[ligA][colA]
    else :
        return None

if __name__=='__main__':

    # 9 FONCTIONS
    nbJoueurs = 2
    nbTresors = 8
    plateau = Plateau(nbJoueurs,nbTresors)
    cartes = creerCartesAmovibles(1, nbTresors)

    tmp = 0
    for carte in cartes :
        if getTresor(carte):
            tmp += 1
    assert tmp == nbTresors, "Plateau"

    assert len(cartes) == 34, "creerCartesAmovibles"
    for carte in cartes :
        assert estValide(carte), "creerCartesAmovibles"

    mettreTresor(getMatrice(plateau)[0][0], 100)
    assert prendreTresorPlateau(getMatrice(plateau), 0, 0, 100), "prendreTresorPlateau"
    assert not prendreTresorPlateau(getMatrice(plateau), 0, 0, 100), "prendreTresorPlateau"

    mettreTresor(getMatrice(plateau)[5][5], 100)
    assert getCoordonneesTresor(getMatrice(plateau), 100) == (5, 5), "getCoordonneesTresor"


    poserPion(getMatrice(plateau)[5][5], 5)
    assert getCoordonneesJoueur(getMatrice(plateau), 5) == (5,5), "getCoordonneesJoueur"

    prendrePionPlateau(getMatrice(plateau), 5, 5, 5)
    assert getCoordonneesJoueur(getMatrice(plateau), 5) == None, "poserPionsPlateau"

    poserPionPlateau(getMatrice(plateau), 2, 2, 3)
    assert getCoordonneesJoueur(getMatrice(plateau), 3) == (2,2), "poserPionsPlateau"


    decoderMurs(getMatrice(plateau)[0][0], 0)
    decoderMurs(getMatrice(plateau)[1][0], 0)
    decoderMurs(getMatrice(plateau)[1][1], 0)
    decoderMurs(getMatrice(plateau)[1][2], 0)
    decoderMurs(getMatrice(plateau)[2][2], 0)
    assert accessible(getMatrice(plateau), 0, 0, 2, 2), "accessible"
    decoderMurs(getMatrice(plateau)[2][2], 15)
    assert not accessible(getMatrice(plateau), 0, 0, 2, 2), "accessible"

    decoderMurs(getMatrice(plateau)[2][2], 0)
    assert accessibleDist(getMatrice(plateau), 0, 0, 2, 2), "accessibleDist"
    decoderMurs(getMatrice(plateau)[2][2], 15)
    assert not accessibleDist(getMatrice(plateau), 0, 0, 2, 2), "accessibleDist"
