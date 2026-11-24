import db
import modeles

COLONNES_BILAN = (
    "id, chiffre_affaires, resultat_net, actifs_courants, passifs_courants, "
    "dettes_totales, capitaux_propres, total_actifs, `date`, societe_sym"
)
COLONNES_COURS = "id, dernier_prix, volume, `date`, societe_sym"


def read_societe(symbole):
    conn = db.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT symbole, nom, secteur_action, pays "
                "FROM societe WHERE symbole = %s",
                (symbole,),
            )
            ligne = cur.fetchone()
        if ligne is None:
            return None
        return modeles.Societe(**ligne)
    finally:
        conn.close()


def read_bilans(symbole):
    conn = db.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT {COLONNES_BILAN} FROM bilan "
                "WHERE societe_sym = %s ORDER BY `date`",
                (symbole,),
            )
            lignes = cur.fetchall()
        return [modeles.Bilan(**ligne) for ligne in lignes]
    finally:
        conn.close()


def read_cours(symbole):
    conn = db.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT {COLONNES_COURS} FROM cours "
                "WHERE societe_sym = %s ORDER BY `date`",
                (symbole,),
            )
            lignes = cur.fetchall()
        return [modeles.Cours(**ligne) for ligne in lignes]
    finally:
        conn.close()
