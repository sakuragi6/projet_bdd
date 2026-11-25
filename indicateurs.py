def calcul_marge_nette(resultat_net, chiffre_affaires):
    try:
        r = (resultat_net / chiffre_affaires) * 100
        return round(r, 2)
    except (ZeroDivisionError, TypeError, ValueError):
        print("Erreur : Calcul impossible")
        return None

def calcul_liquidite(actifs_courants, passifs_courants):
    try:
        r = (actifs_courants / passifs_courants)
        return round(r, 2)
    except (ZeroDivisionError, TypeError, ValueError):
        print("Erreur : Calcul impossible")
        return None

def endettement(dettes_totales, capitaux_propres):
    try:
        r = (dettes_totales / capitaux_propres)
        return round(r, 2)
    except (ZeroDivisionError, TypeError, ValueError):
        print("Erreur : Calcul impossible")
        return None

def calcul_rendement(cours_debut, cours_fin):
    try:
        r = ((cours_fin - cours_debut) / cours_debut) * 100
        return round(r, 2)
    except (ZeroDivisionError, TypeError, ValueError):
        return None

def moyenne_mobile(liste, fenetre):
    if fenetre < 1:
        print("Erreur: Fenêtre incorrecte")
        return None
    if not liste:
        print("Erreur: Liste vide")
        return None
    try:
        r = []
        for i in range(len(liste)):
            debut = max(0, i - fenetre + 1)
            l = liste[debut : i + 1]
            r.append(sum(l) / len(l))
        return r
    except (ZeroDivisionError, TypeError, ValueError):
        print("Erreur : Calcul impossible")
        return None
