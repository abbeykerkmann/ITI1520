def convertSid(siderale):
    resultat = (siderale) * 31558464
    return resultat20
siderale = float(input("veuillez entrer le nombre d'annees siderales:"))
sec = float(convertSid(siderale))
print("Le nombre de secondes-lumiere est: ", sec)
def convertSec(sec):
    resultat = (sec*300000)
    return resultat
seclum = convertSec(sec)
print("la distance est: ", seclum, "km.")
siderale = float(input("Entrez la distance de la première étoile, en années-lumière:"))
sec = float(convertSid(siderale))
print("le nombre de secondes-lumiere est: ",sec)
sec_lum=convertSec(sec)
print("la distance est: ", seclum, "km.")
d1 = seclum
siderale = float(input("Entrez la distance de la deuxieme étoile, en années-lumière:"))
sec = float(convertSid(siderale))
print("le nombre de secondes-lumiere est: ", sec)
seclum = convertSec(sec)
print("la distance est de:",seclum,"km.")
dis= seclum + d1
print("La distance entre les deux étoiles est",dis,"km.")
