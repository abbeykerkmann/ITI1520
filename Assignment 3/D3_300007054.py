import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    print("Shuffling the deck...")
    shuffled = []
    mod = deck.copy() # creer un copy du liste originale
    i = 0
    maximum = len(mod)
    while(i < maximum): 
        index = random.randint(0, (len(mod) - 1)) # creer un nombre au hasard
        shuffled.append(mod.pop(index)) # copier les elements dans la liste au hasard
        maximum = len(mod)
    for i in range(len(deck)):
        deck[i] = shuffled[i] # modifier le liste originale

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 
    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nAppuyez sur Entree pour continuer")
    print("\n" * 50)

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # VOTRE CODE VA ICI
    p1 -= 1
    p2 -= 1
    if(p1 < 0 or p1 > len(discovered) or p2 < 0 or p2 > len(discovered)):
        print("Vous avez entre un position qui n'est pas inclue.")
        print("SVP essayez encore. Cette suposition n'a pas compte.")
    elif(discovered[p1] != "*" or discovered[p2] != "*"):
        print("L'un ou l'autre de vos postes choisis a été jumelé.")
        print("SVP essayez encore. Cette suposition n'a pas compte.")
    elif(p1 == p2):
        print("Vous avez choisi la meme position.")
        print("SVP essayez encore. Cette suposition n'a pas compte.")
    else:
        discovered[p1] = original_board[p1]
        discovered[p2] = original_board[p2]
        print_board(discovered)
        if(discovered[p1] != discovered[p2]):
            discovered[p1] = "*"
            discovered[p2] = "*"
            
        

#############################################################################################
#   FONCTIONS POUR OPTION 1 (avec une plate-forme (board) qui sera lue a partir d'un fichier#
#############################################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarily be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nOn enleve une de chaque carte qui apparaît un nombre impair de fois et enleve toutes les étoiles ...\n")
    maxx = len(l)
    i = 0
    while(i < maxx):
        if(l[i] == "*"): # retirer les etoiles
            del l[i]
            maxx = len(l)
        else:
            i += 1
    j = 0
    max2 = len(l)
    while(j < max2):
        counter = 0
        k = 0
        while(k < max2):
            if(l[j] == l[k]): # compter les instances de chaque lettre
                counter += 1
            k += 1
        if(counter % 2 != 0): # enlève un des lettres qui apparaissent un nombre impair de fois
            del l[j]
            max2 = len(l)
        else:
            j += 1
    return l

def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''
    # VOTRE CODE VA ICI
    results = [0] * len(l)
    for i in range(len(l)):
        counter = 0
        for j in range(len(l)):
            if(l[i] == l[j]):
                counter += 1 # compter les instances de chaque carte
        if(counter == 2): # si il y a 2 instances du carte, retourner Vrai
            results[i] = True
        else: # sinon, Faux
            results[i] = False
    print(results)
    return all(results)
                
        

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''
    print("Prete a jouer...\n")
    # c'est la fonction qui joue le jeu
    # VOTRE CODE VA ICI
    discovered = ["*"] * len(board) # creer un deck plein d'etoiles
    gameover = False
    guesses = 0 # le nombre de supositions
    while(not gameover):
        print_board(discovered) # montre le bord au utilisateur
        print("\n")
        print("Enter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, " + str(len(board)) + "]")
        p1 = int(input("Entrez position 1: ")) # demande a l'utilisateur pour des positions
        p2 = int(input("Entrez position 2: "))
        guesses += 1
        print_revealed(discovered, p1, p2, board)
        if(discovered == board): # si tous les positions sont trouvees
            gameover = True
            break
        wait_for_player()
    # emprimer le message finale au joueur
    print("\nFelicitations! Vous avez complete le jeu en " + str(guesses) + " supositions. C'est " + str(guesses - (len(board) // 2)) + " plus que le mieux possible.")



# PROGRAMME PRINCIPAL (main)
print("Bienvenue au jeu Concentration!")
   
# VOTRE CODE pour l'option 1 ou l'option 2 du joueur VA ICI
option = int(input("Voulez-vous (entrez 1 or 2 pour votre choix):\n(1) d'avoir un deck rigoureux genere pour vous\n(2) ou, charger la partie a partir d'un fichier? "))
while(option != 1 and option != 2):
    print(option + "n'existe pas. SVP essayez encore. Entrez 1 ou 2 pour votre choix")                       
    option = int(input())
#  VOTRE CODE POUR OPTION 1 VA ICI
# Pour option 1 vous aurrez besoin de faire l'appel suivant:
# board=create_board(size)
if(option == 1):
    print("Vous avez choisi d'avoir un deck rigoureux genere pour vous.")
    size = int(input("\nCombien de cartes voulez-vous jouer avec?\nEntrez un nombre pair entre 0 et 52: "))
    while(size % 2 != 0): # si la longeur n'est pas pair
        size = int(input("\nCombien de cartes voulez-vous jouer avec?\nEntrez un nombre pair entre 0 et 52: "))
    while(size > 52 or size < 0): # si la longeur est plus petit que 0 ou plus grand que 52
        size = int(input("\nCombien de cartes voulez-vous jouer avec?\nEntrez un nombre pair entre 0 et 52: "))
    while(size == 0): # si le deck est vide
        print("Vous ne pouvez pas jouer avec un deck vide.")
        size = int(input("\nCombien de cartes voulez-vous jouer avec?\nEntrez un nombre pair entre 0 et 52: "))
    # creer le deck et jouer le jeu
    board = create_board(size)
    shuffle_deck(board)
    wait_for_player()
    play_game(board)

# VOTRE CODE POUR OPTION 2 VA ICI
# Pour option 2 vous aurrez besoin de faire executer les 4 lignes suivantes une apres l'autre
#
#print("Vous choisissez de charger la partie a partir d'un fichier")
#file=input("Entrer le nom du fichier: ")
#file=file.strip()
#board=read_raw_board(file)
#board=clean_up_board(board)
if(option == 2):
    print("Vous choisissez de charger la partie a partir d'un fichier")
    # prend le nom du fichier du joueur
    file = input("Entrer le nom du fichier: ")
    file = file.strip()
    board = read_raw_board(file)
    # nettoyer le deck
    board = clean_up_board(board)
    while(len(board) == 0): # si le deck est vide
        print("Vous ne pouvez pas jouer avec un deck vide.")
        file = input("SVP Entrer le nom d'un autre fichier: ")
        file = file.strip()
        board = read_raw_board(file)
        # nettoyer le deck
        board = clean_up_board(board)
    # creer le deck et jouer le jeu
    shuffle_deck(board)
    wait_for_player()
    play_game(board)
        

