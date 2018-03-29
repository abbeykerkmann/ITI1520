monnaie = float(input("Entrer le montant en dollars:")) * 100
quarters = (monnaie // 25)
dimes = (monnaie % 25) // 10
nickels = ((monnaie % 25) % 10) // 5
pennies = (((monnaie % 25) % 10) % 5) // 1
total = quarters + dimes + nickels + pennies
total = int(total)
print("le nombre de pieces minimal est de:",total)
