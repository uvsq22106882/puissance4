#############################
#GROUPE TD 3 
#BOUDINAR LOUNES 22106882
#SUBRAMANIAM SUYAN 22107171 
#SAMBE Momar 22000621

#https://github.com/uvsq22106882/puissance4.git

#import 
import tkinter as tk
import random as rd 
from random import randint 
#initialisation des variables 
n=5
z=5
x=0
y=0
d=0
t=True
l=True
c=rd.randint(1,2)
total=0
#interface 
racine=tk.Tk()
racine.title("puissance 4")
canvas=tk.Canvas(racine, bg="blue" , height=500 , width=500)
#Fonctions 
def terrain_de_jeu():
    global n, z , l
    while l==True :
        for i in range(7):
            for j in range(7):
                canvas.create_oval(n,z,n+70,z+70, fill="white" , outline="black")
                n=n+70
            z=z+70
            n=5
        l=False   
def player():
    global t , c
    while t==True: 
        if c%2==0 :
            canvas.create_text(250 , 250 , text="le joueur 1 commence " , fill="black" , font=("calibri","22")) 
        else : 
            canvas.create_text(250, 250 , text ="le joueur 2 commence " , fill="black" , font=("calibri" , "22"))
        t=False
Tableau=[[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]
#Définir dans quelle colonne est le clic
def Colonnes(xclic):
    colonne=(xclic)//(70) 
    return colonne

def Lignes(colonne):
    ligne1=0
    for i in range (8):        #Vérifier si des jetons sont déjà présent dans la colonne pour choisir la ligne
        if Tableau[ligne1][colonne]==0:
            ligne=ligne1
        else:
            ligne1=ligne1+1
    return ligne

def jeton (event):
    global Tableau 
    global c , total , x , y
    xclic,yclic=event.x , event.y
    if 0<xclic<500 and 0<yclic<500: #Vérifier que le clic est dans le tableau
        colonne=Colonnes(xclic)
        ligne=Lignes(colonne)
        if c==1: #tour joueur rouge
            canvas.create_oval(colonne*70,ligne*70,colonne*70+75,ligne*70+75, fill="red") #Placement du jeton au milieu de la case
            c=2
            print("C'est au tour du joueur 2")
            Tableau[ligne][colonne]=1      #Définir que cette case est rouge dans le tableau
            total=total+1
        elif c==2: #Tour du joueur jaune
            canvas.create_oval(colonne*70,ligne*70,colonne*70+75,ligne*70+75, fill="yellow")
            c=1
            print("C'est au tour du joueur 1")
            Tableau[ligne][colonne]=2
            total=total+1
    if total==49: #Vérification de tout les jetons placés pour l'égalité
        print("égalité")
canvas.bind("<Button-1>", jeton)



#Bouttons 
Bouton=tk.Button(racine, command=terrain_de_jeu  , text ="Generation de terrain de jeu" , font=("calibri" , "17") ) 
Bouton1=tk.Button(racine, command=player , text=("Quel joueur commence") , font=("Calibri" , "17"))



#positionnement 
canvas.grid()
Bouton.grid(row=0,column=2)
Bouton1.grid(row=0,column=1)


#Affichage de la fenetre 
racine.mainloop()
