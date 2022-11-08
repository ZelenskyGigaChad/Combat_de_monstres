import random

niveau_vie = 20
jouer = True
force_adversaire = 0

while jouer:
   force_adversaire = random.randint(1,5)
   print("Vous tombez face à face avec un adversaire de difficulté :", force_adversaire)
   choix = input("Que voulez-vous faire ? \n1- Combattre cet adversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie \nVotre choix : ")
   if choix == "1":
       if force_adversaire > niveau_vie:
           niveau_vie -= force_adversaire
           print("Vous avez perdu", force_adversaire, "points de vie. Il vous reste", niveau_vie, "points de vie.")
       elif force_adversaire < niveau_vie:
           niveau_vie += force_adversaire
           print("Vous avez gagné", force_adversaire, "points de vie. Il vous reste", niveau_vie, "points de vie.")
   if niveau_vie <= 0:
       print("Vous êtes mort.")
       jouer = False

   elif choix == "2":
       print("Vous avez choisi de contourner cet adversaire.")

   elif choix == "3":
       print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.La partie se termine lorsque les points de vie de l’usager tombent sous 0.L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

   elif choix == "4":
       print("Vous avez choisi de quitter la partie.")
       jouer = False
