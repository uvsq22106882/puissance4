################################

L1-MIASHS Groupe TD 2

GROUPE 3

PROJET PUISSANCE 4   

https://github.com/uvsq22106882/puissance4.git 

Membres du groupe : 

  BOUDINAR LOUNES   22106882

  SAMBE Momar       22000621

  Subramaniam Suyan 22107171

  Kaouachi yota     22008227

################################
Règles du jeu:

Chaque joueur dispose de plusieurs jetons, et chacun d'entre eux doit tenter d'empêcher l'autre d'aligner ses jetons. La victoire est attribuée à celui qui réussit à aligner ses jetons ( 4 ) que ce soit en diagonale, horizontale ou verticale gagne.

Le programme s'est fait en trois étapes:

*La première étape est donc la génération du terrain de jeu avec la présence d’un quadrillage de 7 colonnes et 7 lignes soit 49 cercles.  

*La seconde étape est celle de placement, où l'on a positionné les jetons pour chaque joueur, devant le plateau. Cette première phase utilise le clic gauche de la souris.

*La troisième étape consiste au déplacement des pions et de définir le vainceur de la partie : le moment de jeu où chaque joueur tente de bloquer son adversaire, ou lui mettre un déplacement décisif.

Lors de chaque manche qui passe, la couleur des jetons peut changer pour les joueurs, suivant un tirage aléatoire(1 pour rouge et 2 pour jaune).

Le programme s'exécute à plusieurs reprises, et le premier joueur réussissant à gagner 3 points(chaque manche est un point) remporte la partie, le score apparaissant au-dessus du plateau de jeu.


PROBLEME RENCONTRER Non résolu:

###Pour cette dernière partie, nous avons rencontré des difficultés, de ce fait, nous ne l’avons pas ajouté dans le programme final pour qu’il puisse fonctionner sans soucis ###

###Faire arreter le jeu apres que un joueur ait gagné 

###Faire enregistrer la partie , nous avons utilisé les fonctions de fichiers et de sauvegrade utilisés avec le projet tas de sable mais le programme ne marchait pas 

###Annulation du dernier coup , nous avons pensé a faire un delete mais ca n'a pas marcher puis un destroy , pour au final utiliser un after_cancel mais la fonction ne marche toujours pas 

###Faire apparaitre les jetons de bas en haut , Probleme résolu avec le changment de variable de la fonction Ligne###
