import random

def questions():
    index = 0
    print("SVP donnez les reponses aux additions suivantes")
    repcor = 0
    while(index < 10):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(1, 2)
        if(c == 1):
            print(str(a) + " + " + str(b) + " = ")
            reponse = int(input())
            correct = a+b
            if(reponse != correct):
                print("Incorrect - la reponse est " + str(correct))
            else:
                repcor += 1
        else:
            print(str(a) + " x " + str(b) + " = ")
            reponse = int(input())
            correct = a*b
            if(reponse != correct):
                print("Incorrect = la reponse est " + str(correct))
            else:
                repcor += 1
        index += 1
    print(str(repcor) + " reponses correctes.")
    if(repcor > 6):
        print("Felicitations!")
    else:
        print("Demandez a votre enseignant(e) de vous aider.")

print("Ce logiciel va effectuer un test avec 10 questions.")
questions()
