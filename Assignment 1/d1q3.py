def livresEtOncesEnKilo (livres, onces):
    kilo = 0
    kilo += (livres * 0.453592)
    kilo += (onces * 0.0283495)
    return "Valeur en kilogrammes: " + str(kilo)

livres = float(input("Entrez le nombre de Livres: "))
onces = float(input("Entrez le nombre d'onces: "))
print(livresEtOncesEnKilo(livres, onces))
