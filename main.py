#Renaud Deschênes 401
#2020-11-24
#Jeu de combat

#On importe les modules
import random

#On initialise les variables
niveau_vie = 20
jouer = True
force_adversaire = 0
numero_adversaire = 0
combat_gagnee = 0
combat_perdu = 0
combats = 0
lancer_de_des = 0
victoire_consecutives = 0

#ON cree notre fonction de combat
def combat():

    global combats
    global combat_gagnee
    global combat_perdu
    global victoire_consecutives
    global niveau_vie
    combats += 1
    print('Numero adversaire', numero_adversaire, '\nForce de l\'adversaire :', force_adversaire, '\nNiveau de vie :',
          niveau_vie, '\nNumero du Combat :', combats, '\nCombat gagné :', combat_gagnee, '\nCombat perdu :',
          combat_perdu)
#On roule le de
    lancer_de_des1 = random.randint(1, 6)
    lancer_de_des2 = random.randint(1, 6)
    lancer_de_des = lancer_de_des1 + lancer_de_des2
    print('Vous avez fait un', lancer_de_des1, 'et un', lancer_de_des2, 'soit un total de', lancer_de_des)
#On compare le de avec la force de l'adversaire
    if lancer_de_des > force_adversaire:
        victoire_consecutives += 1
        print('Vous avez gagné le combat')
        combat_gagnee += 1
        niveau_vie += force_adversaire
        print('Niveau de vie :', niveau_vie)
        print('Vous avez gagné 1 point de vie')
    if lancer_de_des <= force_adversaire:
        victoire_consecutives = 0
        print('Vous avez perdu le combat')
        combat_perdu += 1
        niveau_vie -= force_adversaire
        print('Vous avez perdu un point de vie')
        print('Niveau de vie :', niveau_vie)
    print('\n')

#On cree notre fonction pour contourné les adversaires
def contourner():
    global niveau_vie
    print("Vous avez choisi de contourner cet adversaire.")
    niveau_vie -= 1

#On cree notre fonction pour afficher les regles

#On cree notre fonction pour quitter le jeu
def quitter():
    global jouer
    jouer = False

#On commence notre boucle
while jouer:
    if combat_gagnee == 3:
        force_adversaire = random.randint(2, 6)
    else:
        force_adversaire = random.randint(1,5)

    if niveau_vie <= 0:
        print('Vous avez perdu la partie')
        jouer = False

    print("Vous tombez face à face avec un adversaire de difficulté :", force_adversaire)
    numero_adversaire += 1
    choix = input("Que voulez-vous faire ? "
                  "\n1- Combattre cet adversaire"
                  "\n2- Contourner cet adversaire et aller ouvrir une autre porte"
                  "\n3- Afficher les règles du jeu"
                  "\n4- Quitter la partie "
                  "\nVotre choix : ")
#On cree toutes les options de repsonse
    if choix == "1":
        combat()

    elif choix == "2":
        contourner()

    elif choix == "3":
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  "
              "\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
              "\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  "
              "\nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
              "\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0."
              "\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie."
              "\n")
    elif choix == "4":
        quitter()

