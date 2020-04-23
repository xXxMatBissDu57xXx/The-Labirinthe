# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# constructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    matrice = [[0 for x in range(nbColonnes)] for y in range(nbLignes)]
    
    for ligne in range(nbLignes):
        for colonne in range(nbColonnes):
            matrice[ligne][colonne] = valeurParDefaut
    return matrice

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    
    return len(matrice)

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    
    return len(matrice[0])

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """

    return matrice[ligne][colonne]

def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """

    matrice[ligne][colonne] = valeur
    pass


#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    tmp = matrice[numLig][0]
    for i in range(getNbColonnes(matrice)-1):
        matrice[numLig][i] = matrice[numLig][i+1]
    matrice[numLig][getNbColonnes(matrice)-1] = nouvelleValeur
    return tmp

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    tmp = matrice[numLig][getNbColonnes(matrice)-1]
    for i in range(getNbColonnes(matrice)-1, 0,-1):
        matrice[numLig][i] = matrice[numLig][i-1]
    matrice[numLig][0] = nouvelleValeur
    return tmp

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    tmp = matrice[0][numCol]
    for i in range(getNbLignes(matrice)-1):
        matrice[i][numCol] = matrice[i+1][numCol]
    matrice[getNbColonnes(matrice)-1][numCol] = nouvelleValeur
    return tmp

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    tmp = matrice[getNbLignes(matrice)-1][numCol]
    for i in range(getNbLignes(matrice)-1, 0, -1):
        matrice[i][numCol] = matrice[i-1][numCol]
    matrice[0][numCol] = nouvelleValeur

    return tmp

if __name__=='__main__':

    # 9 FONCTIONS

    matrice = Matrice(2,2,0)
    assert matrice == [[0,0],[0,0]], "Matrice"

    assert getNbColonnes(matrice) == 2, "getNbColonnes"

    assert getNbLignes(matrice) == 2, "getNbLignes"
    
    assert getVal(matrice, 0, 0) == 0, "getVal"
    matrice[1][1] = 4
    assert getVal(matrice, 1, 1) == 4, "getVal"

    setVal(matrice, 0,0, 1)
    assert matrice[0][0] == 1, "setVal"

    assert decalageLigneAGauche(matrice,1, 5)==0, "decalageLigneAGauche"
    assert matrice[1][1] == 5, "decalageLigneAGauche"

    assert decalageLigneADroite(matrice,0, 2)==0, "decalageLigneADroite"
    assert matrice[0][0] == 2, "decalageLigneAGauche"

    assert decalageColonneEnBas(matrice,1, 3)==5, "decalageColonneEnBas"
    assert matrice[0][1] == 3, "decalageColonneEnBas"

    assert decalageColonneEnHaut(matrice,0, 5)==2, "decalageColonneEnHaut"
    assert matrice[1][0] == 5, "decalageColonneEnHaut"