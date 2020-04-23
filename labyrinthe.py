# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module labyrinthe
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueurs import *
from plateau import *


def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible 
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 49
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    labyrinthe = {"plateau": Plateau(len(nomsJoueurs), nbTresors), "joueurs": ListeJoueurs(nomsJoueurs), "phase":1, "interdit":(0,0)}

    distribuerTresors(labyrinthe["joueurs"],nbTresors, nbTresorsMax)
    initAleatoireJoueurCourant(labyrinthe["joueurs"])
    return labyrinthe

def getPlateau(labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    return getMatrice(labyrinthe["plateau"])

def getNbParticipants(labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return getNbJoueurs(labyrinthe["joueurs"])

def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return nomJoueurCourant(labyrinthe["joueurs"])

def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return numJoueurCourant(labyrinthe["joueurs"])

def getPhase(labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """   
    return labyrinthe["phase"]


def changerPhase(labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """    
    if labyrinthe["phase"] == 1 :
        labyrinthe["phase"] = 0
    else :
        labyrinthe["phase"] = 1


def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """    
    nbTresor = 0
    for ligne in getMatrice(labyrinthe["plateau"]):
        for case in ligne :
            if getTresor(case):
                nbTresor += 1
    return nbTresor

def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py    
    """
    return labyrinthe["joueurs"]

def enleverTresor(labyrinthe,lin,col,numTresor):
    """
    enleve le trésor numTresor du plateau du labyrinthe. 
    Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
    est diminué de 1
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """    
    prendreTresorPlateau(labyrinthe["plateau"], lin, col, numTresor)

def prendreJoueurCourant(labyrinthe,lin,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe    
    """
    prendrePionPlateau(labyrinthe["plateau"], lin, col, numJoueurCourant(labyrinthe["joueurs"]))

def poserJoueurCourant(labyrinthe,lin,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe     
    """
    poserPionPlateau(labyrinthe["plateau"], lin, col, numJoueurCourant(labyrinthe["joueurs"]))

def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer    
    """    
    return labyrinthe["plateau"]["carte"]

def coupInterdit(labyrinthe,direction,rangee):
    """ 
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    return (direction, rangee) == labyrinthe["interdit"]

def jouerCarte(labyrinthe,direction,rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passées 
    en paramètres. Cette fonction
       - met à jour le plateau du labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """
    if direction == 'N' :
        changerCarte(labyrinthe["plateau"], decalageColonneEnBas(getMatrice(labyrinthe["plateau"]), rangee, getCarteAJouer(labyrinthe)))
    if direction == 'S' :
        changerCarte(labyrinthe["plateau"], decalageColonneEnHaut(getMatrice(labyrinthe["plateau"]), rangee, getCarteAJouer(labyrinthe)))
    if direction == 'O' :
        changerCarte(labyrinthe["plateau"], decalageLigneADroite(getMatrice(labyrinthe["plateau"]), rangee, getCarteAJouer(labyrinthe)))
    if direction == 'E' :
        changerCarte(labyrinthe["plateau"], decalageLigneAGauche(getMatrice(labyrinthe["plateau"]), rangee, getCarteAJouer(labyrinthe)))

def tournerCarte(labyrinthe,sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyritnthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe    
    """
    if sens == 'H' :
        tournerHoraire(getCarte(labyrinthe["plateau"]))
    if sens == 'A' :
        tournerAntiHoraire(getCarte(labyrinthe["plateau"]))

def getTresorCourant(labyrinthe):
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: le numéro du trésor recherché par le joueur courant
    """
    return tresorCourant(labyrinthe["joueurs"])

def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du trésor à chercher ou None si celui-ci 
              n'est pas sur le plateau
    """
    for ligne in range(7):
        for case in range(7):
            if getTresorCourant(labyrinthe) == getTresor(getMatrice(labyrinthe["plateau"])[ligne][case]) :
                return ligne, case
    return None

def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du joueur courant ou None si celui-ci 
              n'est pas sur le plateau
    """
    for ligne in range(7):
        for case in range(7):
            if getNumJoueurCourant(labyrinthe)+1 in getListePions(getMatrice(labyrinthe["plateau"])[ligne][case]) :
                return ligne, case
    return None

def executerActionPhase1(labyrinthe,action,rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: labyrinthe: le labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et rangee est un des chiffre 1,3,5 
                        => insèrer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """
    if action == 'T' :
        tournerCarte(labyrinthe)
        return 0
    elif action in ['N', 'S', 'O', 'E'] and rangee in [1, 3, 5]:
        if coupInterdit(labyrinthe, action, rangee):
            return 2
        jouerCarte(labyrinthe, action, rangee)
        changerPhase(labyrinthe)
        return 1
    elif type(action) == type(rangee) == type(1) :
        return 3
    return 4
    
def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: labyrinthe le labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    ligD, colD = getCoordonneesJoueurCourant(labyrinthe["plateau"])
    accessibleDist(labyrinthe["plateau"], ligD, colD, ligA, colA)

def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    if getCoordonneesTresorCourant(labyrinthe) == getCoordonneesJoueurCourant(labyrinthe) :
        joueurCourantTrouveTresor(getListeJoueurs(labyrinthe))
        if joueurCourantAFini(getListeJoueurs(labyrinthe)) :
            return 2
        else :
            return 1
    else :
        return 0
    changerPhase(labyrinthe)

if __name__=="__main__":
    pass
