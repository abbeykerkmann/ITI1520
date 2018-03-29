### Je ne pouvais pas trouver un partenaire pour ce travail
### J'ai meme poste sur facebook mais je n'ai eu aucune reponse
### J'espere que ca c'est d'accord

def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
    # a completer
    
    # retourne rien
   for i in range(len(tab)): # pour voir les rangees
      for j in range(len(tab[i])): #pour voir les colonnes
         tab[i][j] == '-' # ajoute les -

      
def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''

    # a completer
    if(testLignes(tab) == 'X' or testCols(tab) == 'X' or testDiags(tab) == 'X'):
       print("Joueur X a gagne!") # si les valeurs des fonctions sont X, X gagne le jeu
       return True
    elif(testLignes(tab) == 'O' or testCols(tab) == 'O' or testDiags(tab) == 'O'):
       print("Joueur O a gagne!") # si les valeurs des fonctions sont O, O gagne le jeu
       return True
    elif(testMatchNul(tab)):
       print("Match nul") # si le tableus ne contient pas de - et personne gagne, c'est un match nul
       return True
    return False  # a changer

 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   for i in range(len(tab)):
      countX = 0 # les variables qui vont compter le nombre de X et O
      countO = 0
      for j in range(len(tab[i])):
         if(tab[i][j] == 'X'): # compter le nombre de X dans chaque rangee
            countX += 1
         elif(tab[i][j] == 'O'): # compter le nombre de O dans chaque rangee
            countO += 1
      if(countX == 3): # si le nombre de X est 3, retourne X comme gagnant
         return 'X'
      elif(countO == 3): # si le nombre de O est 3, retourne O comme gagnant
         return 'O'
   return '-' # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant 

  
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   for i in range(len(tab[0])):
      countX = 0 # les variables qui vont compter le nombre des X et O
      countO = 0
      for j in range(len(tab)):
         if(tab[j][i] == 'X'): # compter le nombre de X dans chaque colonne
            countX += 1
         elif(tab[j][i] == 'O'): # compter le nombre de O dans chaque colonne
            countO += 1
      if(countX == 3): # si le nombre de X est 3, retourne X comme gagnant
         return 'X'
      elif(countO == 3): # si le nombre de O est 3, retourne O comme gagnant
         return 'O' 
   return '-'   #a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

   
def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   countX = 0 # les variables qui vont compter le nombre des X et O
   countO = 0
   for i in range(len(tab)):
      if(tab[i][i] == 'X'): # compter les X dans le diagonal de 0,0 a 2,2
         countX += 1
      elif(tab[i][i] == 'O'): # compter les O dans le diagonal de 0,0 a 2,2
         countO += 1
   if(countX == 3): # si le nombre de X est 3, retoure X comme gagnant
      return 'X'
   elif(countO == 3): # si le nombre de O est 3, retourne O comme gagnant
      return 'O'
   countX = 0 # 
   countO = 0
   for i in range(len(tab) - 1, 0, -1):
      if(tab[i][i] == 'X'): # compter les X dans le diagonal de 2,0 a 0,2
         countX += 1
      elif(tab[i][i] == 'O'): # compter les O dans le diagonal de 2,0 a 0,2
         countO += 1
   if(countX == 3): # si le nombre de X est 3, retourne X comme gagnant
      return 'X'
   elif(countO == 3): # si le nombre de O est 3, retourne O comme gagnant
      return 'O'
   return '-'   # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

  
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   for i in range(len(tab)):
      for j in range(len(tab[i])):
         if(tab[i][j] == '-'): # si un element dans la matrice est un -, ce n'est pas un match nul
            return False
   return True

