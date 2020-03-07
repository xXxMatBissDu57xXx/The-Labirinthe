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

def Carte(nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """

    carte = {"nord":nord, "est":est, "sud":sud, "ouest":ouest, "tresor":tresor, "pions":pions}
    return carte

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """

    if([c["nord"],c["est"],c["sud"],c["ouest"]].count(1)<3):
        return True
    else:
        return False

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """

    if(c["nord"]):
        return True
    else:
        return False

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """

    if(c["sud"]):
        return True
    else:
        return False

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """

    if(c["est"]):
        return True
    else:
        return False

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """

    if(c["ouest"]):
        return True
    else:
        return False

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """

    return c["pions"]

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """

    c["pions"] = listePions
    pass

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """

    nbPions = 0
    for i in getListePions(c):
        nbPions += 1
    return nbPions

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """

    for i in c.get("pions"):
        if i == pion :
            return True
    return False

def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """

    return c["tresor"]

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """

    tresor = getTresor(c)
    c["tresor"] = 0
    return tresor

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """

    tmp = c["tresor"]
    c["tresor"]=tresor
    return tmp

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """

    if possedePion(c, pion):
            c["pions"].remove(pion)

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    pions = getListePions(c)
    
    if not possedePion(c, pion):
        pions.append(pion)
    c["pions"]=pions

def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    
    tmp = c["nord"]
    c["nord"] = c["ouest"]
    c["ouest"] = c["sud"]
    c["sud"] = c["est"]
    c["est"] = tmp
    pass

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    
    tmp = c["nord"]
    c["nord"] = c["est"]
    c["est"] = c["sud"]
    c["sud"] = c["ouest"]
    c["ouest"] = tmp
    pass

def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """

    i = 0
    for i in range(random.randint(0,3)):
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
    
    return c["ouest"]*8+c["sud"]*4+c["est"]*2+c["nord"]

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """    

    c["ouest"] = bool(code//8)
    code %= 8
    c["sud"] = bool(code//4)
    code %= 4
    c["est"] = bool(code//2)
    code %= 2
    c["nord"] = bool(code)

def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """

    return listeCartes[coderMurs(c)]

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """

    if not ((carte1["nord"])or(carte2["sud"])):
        return True
    else : 
        return False

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """

    if not((carte1["sud"])or(carte2["nord"])):
        return True
    else : 
        return False

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """

    if not((carte1["ouest"])or(carte2["est"])):
        return True
    else : 
        return False

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """

    if not((carte1["est"])or(carte2["ouest"])):
        return True
    else : 
        return False

if __name__=='__main__':
    cartes = []
    for i in range(16):
        cartes.append(Carte(False, False, False, False))
        decoderMurs(cartes[i], i)

    c1 = Carte(False, False, False, False)
    c2 = Carte(True, True, True, True)
    
    assert c1 == {"nord":False, "est":False, "sud":False, "ouest":False, "tresor":0, "pions":[]}, "Carte"
    assert c2 == {"nord":True, "est":True, "sud":True, "ouest":True, "tresor":0, "pions":[]}, "Carte"

    assert coderMurs(c1) == 0, "coderMurs"
    assert coderMurs(c2) == 15, "coderMurs"

    decoderMurs(c1,7)
    assert coderMurs(c1) == 7, "decoderMurs"
    decoderMurs(c1,0)


    """VERIFICATION MURS"""
    assert estValide(c1), "estValide"
    assert not estValide(c2), "estValide"

    assert not murNord(c1), "murNord"
    assert murNord(c2), "murNord"

    assert not murEst(c1), "murEst"
    assert murEst(c2), "murEst"

    assert not murSud(c1), "murSud"
    assert murSud(c2), "murSud"

    assert not murOuest(c1), "murOuest"
    assert murOuest(c2), "murOuest"

    assert passageNord(c1, c1), "passageNord"
    assert not passageNord(c2, c2), "passageNord"

    assert passageEst(c1, c1), "passageEst"
    assert not passageEst(c2, c2), "passageEst"

    assert passageSud(c1, c1), "passageSud"
    assert not passageSud(c2, c2), "passageSud"

    assert passageOuest(c1, c1), "passageOuest"
    assert not passageOuest(c2, c2), "passageOuest"

    c3 = Carte(True,True,False,False)
    assert toChar(c3) == listeCartes[3], "toChar"

    tournerHoraire(c3)
    assert toChar(c3) == listeCartes[6], "tournerHoraire"

    tournerAntiHoraire(c3)
    assert toChar(c3) == listeCartes[3], "tournerAntiHoraire"
    
    tourneAleatoire(c3)
    assert toChar(c3) in [listeCartes[3],listeCartes[6],listeCartes[9],listeCartes[12]], "tournerAleatoire"


    """VERIFICATION PIONS"""
    c1["pions"] = [80]
    assert getListePions(c1)==[80], "getListePions"
    c1["pions"] = []

    poserPion(c1,1)
    assert getListePions(c1)==[1], "poserPion"

    setListePions(c1, [2])
    assert getListePions(c1)==[2], "setListePions"

    assert possedePion(c1, 2)==True, "possedePion"
    assert possedePion(c1, 1)==False, "possedePion"

    prendrePion(c1, 2)
    assert possedePion(c1, 1)==False, "prendrePion"

    assert getNbPions(c1)==0, "getNbPions"
    c1["pions"] = [80]
    assert getNbPions(c1)==1, "getNbPions"

    """VERIFICATION TRESOR"""
    c1["tresor"]=80
    assert getTresor(c1)==80, "getTresor"

    assert mettreTresor(c1, 81)==80, "mettreTresor"
    assert getTresor(c1)==81, "mettreTresor"

    assert prendreTresor(c1)==81, "prendreTresor"
    assert getTresor(c1)== 0, "prendreTresor"