from random import shuffle

class Blackjack:
 valeurs={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
  
 def joue(self):
  '''jour un jeu'''   
  d = JeuDeCartes()
  d.battre()
  
  banque = Main('Banque')
  joueur = Main('Joueur')

  # donne deux cartes au joueur et deux cartes a la banque
  for i in range(2):  
    joueur.ajouteCarte(d.tireCarte())
    banque.ajouteCarte(d.tireCarte())

  # montre les mains
  banque.montreMain()
  joueur.montreMain()

  # tant que le joueur demande Carte!, la banque tire des cartes
  reponse = input('Carte? Oui ou non? (Par défaut oui) ')
  while reponse in ['','o','O','oui','Oui']:
    c = d.tireCarte()
    print("Vous avez:")
    print(c)
    joueur.ajouteCarte(c)
    if self.total(joueur) > 21:
       print("Vous avez dépassé 21. Vous avez perdu.")
       return
    reponse = input('Carte? Oui ou non? (Par défaut oui) ')

  # la banque joue avec ses regles  
  while self.total(banque) < 17:
    c = d.tireCarte()
    print("La banque a:")
    print(c)
    banque.ajouteCarte(c)
    if self.total(banque) > 21:
        print("La banque a dépassé 21. Vous avez gagné.")
        return

  # si 21 n'est pas depassée, compare les mains pour trouver le gagnat  
  self.compare(banque, joueur)

      
 def total(self, main):
    ''' (Main) -> int
    calcule la somme des valeur de toutes les cartes dans la main
    '''
    somme = 0
    for i in range(len(main.cartes)):
        if(main.cartes[i].valeur == 'J' or main.cartes[i].valeur == 'Q' or main.cartes[i].valeur == 'K'): # Ajouter la valeur d'un J, Q, ou K
            somme += 10
        elif(main.cartes[i].valeur == 'A'): #ajouter la valeur d'un A
            somme += 11
        else:
            somme += int(main.cartes[i].valeur) #Ajouter la valeur des cartes numeriques
    if(somme > 21): #si la somme est plus grand que 21 et il y a des A, reduire la somme par 10
        for i in range(len(main.cartes)):
            if(main.cartes[i].valeur == 'A'):
                somme -= 10
    return somme #retourne la somme calculee

 def compare(self, banque, joueur):
    ''' (Main, Main) -> None
    Compare la main du joueur avec la main de la banque
    et affiche de messages
    '''
    if(self.total(joueur) == 21): #si la somme du joueur est 21, il gagne
        print("Vous avez gagne.")
    elif(self.total(banque) == 21): #si la somme du banque est 21, la banque gagne
        print("Vous avez perdu.")
    elif(self.total(banque) < self.total(joueur)): #si la somme du banque est plus petit que la somme du joueur, le joueur gagne
        print("Vous avez gagne")
    elif(self.total(banque) > self.total(joueur)): #si la somme du banque est plus grand que la somme du joueur, la banque gagne
        print("Vous avez perdu")
    else: #si il y a une egalite
        print("Egalite")
       
class Main(object):
    '''represente une main des cartes a jouer'''

    def __init__(self, joueur):
        '''(Main, str)-> none
        initialise le nom du joueur et la liste de cartes avec liste vide'''
        self.joueur = joueur #creer le joueur avec un nom
        self.cartes = [] #creer une lste vide des cartes

    def ajouteCarte(self, carte):
        '''(Main, Carte) -> None
        ajoute une carte a la main'''
        self.cartes.append(carte) #ajoute une carte a la liste des cartes

    def montreMain(self):
        '''(Main)-> None
        affiche le nom du joueur et la main'''
        print(self.joueur + ":   " + str(self.cartes[0]) + "   " + str(self.cartes[1])) #montre le nom du joueur avec les cartes dans sa main
                
    def __eq__(self, autre):
        '''retourne True si les main ont les meme cartes
           dans la meme ordre'''
        index = 0
        while(index < len(self.cartes) and index < len(autre.cartes)): 
            if(self.cartes[index] != autre.cartes[index]): #si les cartes ne sont pas les memes, retourner False
                return False
            index += 1
        return True #sinon, retourne True

    def __repr__(self):
        '''retourne une representation de l'objet'''
        return str(self.cartes) #representation des cartes dans la main

class Carte:
    '''represente une carte a jouer'''

    def __init__(self, valeur, couleur):
        '''(Carte,str,str)->None        
        initialise la valeur et la couleur de la carte'''
        self.valeur = valeur
        self.couleur = couleur  # pique, coeur, trefle ou carreau

    def __repr__(self):
        '''(Carte)->str
        retourne une representation de l'objet'''
        return 'Carte('+self.valeur+', '+self.couleur+')'

    def __eq__(self, autre):
        '''(Carte,Carte)->bool
        self == autre si la valeur et la couleur sont les memes'''
        return self.valeur == autre.valeur and self.couleur == autre.couleur

class JeuDeCartes:
    '''represente une jeu de 52 cartes'''
    # valeurs et couleurs sont des variables de classe
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    # couleurs est un set de 4 symboles Unicode qui representent les 4 couleurs
    # pique, coeur, trefle ou carreau
    
    def __init__(self):
        'initialise le paquet de 52 cartes'
        self.paquet = []          # paquet vide au debut
        for couleur in JeuDeCartes.couleurs: 
            for valeur in JeuDeCartes.valeurs: # variables de classe
                # ajoute une Carte de valeur et couleur
                self.paquet.append(Carte(valeur,couleur))

    def tireCarte(self):
        '''(JeuDeCartes)->Carte
        distribue une carte, la premiere du paquet'''
        return self.paquet.pop()

    def battre(self):
        '''(JeuDeCartes)->None
        pour battre le jeu des cartes'''
        shuffle(self.paquet)

    def __repr__(self):
        '''retourne une representation de l'objet'''
        return 'Paquet('+str(self.paquet)+')'

    def __eq__(self, autre):
        '''retourne True si les paquets ont les meme cartes
           dans la meme ordre'''
        return self.paquet == autre.paquet
    
    
b = Blackjack()
b.joue()

