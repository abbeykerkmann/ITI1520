def calcul(monnaie, quarters, dimes, nickels, pennies):
    total = quarters + dimes + nickels + pennies
    return total
monnaie = float(input("Entrer le montant en dollars:")) * 100
quarters = (monnaie // 25)
dimes = (monnaie % 25) // 10
nickels = ((monnaie % 25) % 10) // 5
pennies = (((monnaie % 25) % 10) % 5) // 1
total = int(calcul(monnaie, quarters, dimes, nickels, pennies))
print("Le nombre de pieces minimal est:", total)
