import db
import modeles

def read_societe(symbole):
    conn = db.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT symbole, nom, secteur_action, pays FROM societe WHERE symbole = %s",
                (symbole,),
            )
        ligne = cur.fetchone()
        if ligne is None:
            return None
        return modeles.Societe(**ligne)
    finally:
        conn.close()
