import indicateurs
import depot

sym = input("Entrez le symbole de la société : ")
print("\n")
if isinstance(sym, str) and len(sym) <= 5 and len(sym) > 0:
    soc = depot.read_societe(sym)
    bilans = depot.read_bilans(sym)
    cours = depot.read_cours(sym)
    if soc:
        print(f"=== {soc.nom} ({soc.symbole}) ===")
        print(f"Secteur : {soc.secteur_action} | Pays : {soc.pays}")
        print(f"\n{'Date':<12} | {'CA':>14} | {'Résultat Net':>14} | {'Dettes Tot.':>14} | {'Cap. Propres':>14}")
        print("-" * 78)
        for b in bilans:
            print(
                f"{str(b.date):<12} | "
                f"{b.chiffre_affaires:>14,.0f} | "
                f"{b.resultat_net:>14,.0f} | "
                f"{b.dettes_totales:>14,.0f} | "
                f"{b.capitaux_propres:>14,.0f}"
            )
        print(f"\n{'Date':<12} | {'Dernier Prix':>12} | {'Volume':>15}")
        print("-" * 45)
        for c in cours:
            print(f"{str(c.date):<12} | {c.dernier_prix:>11.2f} € | {c.volume:>15,}")
    else:
        print("Société introuvable.")
else:
    print("Symbole non valide.")

