import indicateurs
import depot

def fmt(valeur, suffixe=""):
    if valeur is None:
        return "indisponible"
    return f"{valeur:.2f}{suffixe}"

sym = input("Entrez le symbole de la société : ")
print("\n")
if isinstance(sym, str) and len(sym) <= 5 and len(sym) > 0:
    try:
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

            print(f"\n{'Date':<12} | {'Marge nette':>12} | {'Liquidité':>12} | {'Endettement':>12}")
            print("-" * 56)
            for b in bilans:
                marge = indicateurs.calcul_marge_nette(b.resultat_net, b.chiffre_affaires)
                liquidite = indicateurs.calcul_liquidite(b.actifs_courants, b.passifs_courants)
                endettement = indicateurs.endettement(b.dettes_totales, b.capitaux_propres)
                print(
                    f"{str(b.date):<12} | "
                    f"{fmt(marge, ' %'):>12} | "
                    f"{fmt(liquidite):>12} | "
                    f"{fmt(endettement):>12}"
                )

            if cours:
                prix = [float(c.dernier_prix) for c in cours]
                rendement = indicateurs.calcul_rendement(prix[0], prix[-1])
                mm = indicateurs.moyenne_mobile(prix, 2)
                print(f"\n{'Rendement':<20} : {fmt(rendement, ' %')}")
                print(f"{'Moyenne mobile (2)':<20} : {mm if mm is not None else 'indisponible'}")

        else:
            print("Société introuvable.")
    except Exception as e:
        print(f"Erreur : {e}")
else:
    print("Symbole non valide.")
