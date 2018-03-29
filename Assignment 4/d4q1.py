### Je ne pouvais pas trouver un partenaire pour ce travail
### J'ai même posté sur facebook mais je n'ai eu aucune réponse
### J'espere que ca c'est d'accord

### Question 1 ###
def ajoute(m):
    for i in range(len(m)): # les rangees du matrice
        for j in range(len(m[i])): # les colonnes du matrice
            m[i][j] += 1 # ajouter 1 a chaque element

def ajoute_v2(m):
    res = [] # creer un nouvelle liste vide
    for i in range(len(m)):
        res2 = [0] * len(m[i]) # creer un nouvelle liste temporaire
        for j in range(len(res2)):
            res2[j] = m[i][j] # ajouter les valeurs du matrice au liste temporaire
        res.append(res2) # ajouter le liste temporaire a la liste vide
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] += 1 # ajouter 1 aux elements dans la nouvelle liste
    return res

print("Entrer les elements de la matrice avec espaces entre les colonnes.\nUne rangee par ligne, et une ligne vide a la fin.")
m = [] # creer une liste vide
nums = str(input()) # prendre le input de l'utilisateur
i = 0
while(nums != ""): # arrete quand l'utilisateur entre rien
    nums = nums.split() # creer une liste de str qui represent les numeraux
    for i in range(len(nums)):
        nums[i] = int(nums[i]) # changer les str en int
    m.append(nums) # ajjouter les int a la matrice
    i += 1
    nums = str(input()) # prend un autre input
print("La matrice est:\n" + str(m))
ajoute(m)
print("Apres execution de la fonction ajoute, la matrice est:\n" + str(m))
m2 = ajoute_v2(m)
print("Une nouvelle matrice creee avec ajoute_v2:\n" + str(m2))
print("Apres execution de la fonction ajoute_v2, la matrice initiale est:\n" + str(m))
