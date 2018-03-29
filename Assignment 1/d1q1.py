livres = input("Entrez le nombre de livres: ")
onces = input("Entrez le nombre d'onces: ")
ltok = float(livres) * 2.2046226218
otok = float(onces) * 0.02834952
kilo = ltok + otok
print(livres + " livres et " + onces + " onces équivalent à " + str(kilo) + " kilogrammes.")
