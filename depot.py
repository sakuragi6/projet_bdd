import db
import modeles

def read_societe(symbole):
    conn = db.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM societe WHERE symbole = %s",
                (symbole,),
            )
            ligne = cur.fetchone()
        if ligne is None:
            return None
        return modeles.Societe(**ligne)
    finally:
        conn.close()

def read_bilan(id):
    conn = db.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM bilan WHERE id = %s",
                (id,),
            )
            ligne = cur.fetchone()
        if ligne is None:
            return None
        return modeles.Bilan(**ligne)
    finally:
        conn.close()

def read_cours(id):
    conn = db.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM cours WHERE id = %s",
                (id,),
            )
            ligne = cur.fetchone()
        if ligne is None:
            return None
        return modeles.Cours(**ligne)
    finally:
        conn.close()





