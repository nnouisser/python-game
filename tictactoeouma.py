import random


place = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
joueur_actuel = "@"
gagnant = None
encours = True
print ("Welcome to @/* game ")
print("choisit * ou @")

def affiche(place):
    print(place[0] + " | " + place[1] + " | " + place[2])
    print("---------")
    print(place[3] + " | " + place[4] + " | " + place[5])
    print("---------")
    print(place[6] + " | " + place[7] + " | " + place[8])



def entre(place):
    inp = int(input("choisi place 1-9: "))
    if place[inp-1] == "-":
        place[inp-1] = joueur_actuel
    else:
        print("cette case est déjà jouée")



def vérifier_horizontalement (place):
    global gagnant
    if place[0] == place[1] == place[2] and place[0] != "-":
        gagnant = place[0]
        return True
    elif place[3] == place[4] == place[5] and place[3] != "-":
        gagnant = place[3]
        return True
    elif place[6] == place[7] == place[8] and place[6] != "-":
        gagnant = place[6]
        return True

def vérification_verticalement(place):
    global gagnant
    if place[0] == place[3] == place[6] and place[0] != "-":
        gagnant = place[0]
        return True
    elif place[1] == place[4] == place[7] and place[1] != "-":
        gagnant = place[1]
        return True
    elif place[2] == place[5] == place[8] and place[2] != "-":
        gagnant = place[2]
        return True



def vérification_diagonale(place):
    global gagnant
    if place[0] == place[4] == place[8] and place[0] != "-":
        gagnant = place[0]
        return True
    elif place[2] == place[4] == place[6] and place[4] != "-":
        gagnant = place[2]
        return True


def gagne(place):
    global encours
    if vérifier_horizontalement(place):
        affiche(place)
        print(f"le gagnant est  {gagnant}!")
        encours = False

    elif vérification_verticalement(place):
        affiche(place)
        print(f"le gagnant est {gagnant}!")
        encours = False

    elif vérification_diagonale(place):
        affiche(place)
        print(f"le gagnant est {gagnant}!")
        encours = False



def finie(place):
    global encours
    if "-" not in place:
        affiche(place)
        print("jeu fini et pas de gagnant")
        encours = False



def j():
    global encours
    global joueur_actuel
    if joueur_actuel == "@":
        joueur_actuel = "*"
    else:
        joueur_actuel = "@"
        ordinateur(place)



def ordinateur(place):
    global joueur_actuel
    if joueur_actuel == "*":
        position = random.randint(0, 8)
        if place[position] == "-":
            place[position] = "*"
            j()


while encours:
    affiche(place)
    entre(place)
    gagne(place)
    finie(place)
    j()
    ordinateur(place)
    gagne(place)
    finie(place)

