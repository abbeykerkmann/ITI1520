def etoiles(n): #pour cette fonction, on doit utiliser la fonction print() pour voir les etoiles dans le format correct
    if(n > 1):
        return (('*' * n) + "\n" + etoiles(n - 1) + "\n" + ('*' * n)) #affiche le premier et dernier ligne d'etoiles en utilisant 'n' avec les autres valeurs de 'n' au milieu
    else:
        return ('*' + "\n" + '*') #quand n est egale a 1, affiche les derniers lignes d'etoiles au milieu

def sommeListePos_rec(l, n):
    if(len(l) == 0): #si la liste est vide, retourne zero
        return 0
    elif(l[0] > 0): #si le premier element du liste est positif, ajouter cette valeur au somme et supprimer cette valeur
        return l.pop(0) + sommeListePos_rec(l, len(l))
    else: #si le premier element n'est pas positif, supprimer cette valeur et ajouter 0 a la somme
        del l[0]
        return 0 + sommeListePos_rec(l, len(l))

