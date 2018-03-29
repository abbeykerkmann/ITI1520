def masseCorporelle(poids, taille):
    bmi = (poids / taille) / taille
    message = ""
    if(bmi < 18.5):
        message = "Maigreur"
    elif(bmi >= 18.5 and bmi < 25):
        message = "Poids Ideal"
    elif(bmi >= 25 and bmi < 30):
        message = "Surpoids"
    else:
        message = "Obesite"
    print("Votre IMC est " + str(bmi) + "\n" + message)

poids = float(input("SVP entre votre poids en kilogrammes: "))
taille = float(input("SVP entre votre taille en metres: "))
masseCorporelle(poids, taille)
