from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass
class Societe:
    symbole: str
    nom: str
    secteur_action: str
    pays: str

@dataclass
class Bilan:
    id: int
    chiffre_affaires: Decimal
    resultat_net: Decimal
    actifs_courants: Decimal
    passifs_courants: Decimal
    dettes_totales: Decimal
    capitaux_propres: Decimal
    total_actifs: Decimal
    date: date
    societe_sym: str

@dataclass
class Cours:
    id: int
    dernier_prix: Decimal
    volume: int
    date: date
    societe_sym: str

