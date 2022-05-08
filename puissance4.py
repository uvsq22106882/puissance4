#############################
#GROUPE TD 3 
#BOUDINAR LOUNES 22106882
#SUBRAMANIAM SUYAN 22107171 
#SAMBE Momar 22000621

#https://github.com/uvsq22106882/puissance4.git

#import 
from struct import pack
import tkinter as tk
import random as rd 
from random import randint
from turtle import end_poly 
#initialisation des variables 
n=5
z=105
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
canvas=tk.Canvas(racine, bg="blue" , height=800 , width=700)
#Fonctions 
def terrain_de_jeu():
    global n, z , l
    while l==True :
        for i in range(7):
            for j in range(7):
                canvas.create_oval(n,z,n+100,z+100, fill="white" , outline="black")
                n=n+100
            z=z+100
            n=5
        l=False   
    canvas.create_rectangle(0, 0, 750, 100, fill="grey")
def player():
    global t , c
    if total == 0:
        if c%2==0 :
            text1 = canvas.create_text(350 , 50 , text ="Le joueur 1 commence" , fill="black" , font=("calibri","22"))
        else : 
            text1 = canvas.create_text(350 , 50 , text ="Le joueur 2 commence", fill="black" , font=("calibri","22"))

Tableau=[[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]
#Définir dans quelle colonne est le clic
def Recherche_colonne(xClic):
    colonne=(xClic)//(100) 
    return colonne

def Recherche_ligne(colonne):
    for i in range(7):        #Vérifier si des jetons sont déjà présents dans la colonne pour choisir la ligne
        p=6-i
        if Tableau[p][colonne]==0:
            ligne=p
            break
        else:
            p=p-1
    return ligne

def jeton (event):
    global Tableau 
    global c , total , x, y
    nb_jeton=0
    xclic,yclic=event.x , event.y
    if 0<xclic<701: #Vérifier que le clic est dans le tableau
        colonne=Recherche_colonne(xclic)
        ligne=Recherche_ligne(colonne)
        if c==1: #tour joueur rouge
            canvas.create_oval(colonne*100+100,ligne*100+110,colonne*100+10,ligne*100+200, fill='red') #Placement du jeton au milieu de la case
            Tableau[ligne][colonne]=1      #Définir que cette case est rouge dans le tableau
            Win = WinCondition()
            total=total+1
            c=2
            print("Au tour du joueur 2")
        elif c==2: #Tour du joueur jaune
            canvas.create_oval(colonne*100+100,ligne*100+110,colonne*100+10,ligne*100+200, fill='yellow')
            Tableau[ligne][colonne]=2
            Win = WinCondition()
            total=total+1
            c=1
            print("Au tour du joueur 1")
    if total == 1:
        canvas.create_rectangle(0,0,750,100, fill="grey")
    if Win == True:
        if c==1:
            canvas.create_text(350 , 50 , text ="Joueur 2 (Jaune) gagne!" , fill="black" , font=("calibri","22"))
            return
        else:
            canvas.create_text(350 , 50 , text ="Joueur 1 (Rouge) gagne!" , fill="black" , font=("calibri","22"))
            return
canvas.bind("<Button-1>", jeton)

def WinCondition():
    for i in range(7):
        for j in range(4):
            if Tableau[i][j]==c:
                counter = 1
                for k in range(3): # vérifier si 4 jetons sont alignés à l'horizontale
                    if Tableau[i][j+k+1]==c:
                        counter += 1
                if counter == 4:
                    Win = True
                    return Win
    for i in range(4):
        for j in range(4):
            if Tableau[i+3][j]==c:
                counter = 1
                for k in range(3): #vérifier si 4 jetons sont alignés en diagonale d'en bas à gauche jusqu'en haut à droite
                    if Tableau[(i+3)-(k+1)][j+k+1]==c:
                        counter += 1
                if counter == 4:
                    Win = True
                    return Win
    for i in range (4):
        for j in range(4):
            if Tableau[i][j]==c:
                counter = 1
                for k in range(3): #vérifier si 4 jetons sont alignés en diagonale d'en haut à gauche jusqu'en bas à droite
                    if Tableau[(i+(k+1))][j+k+1]==c:
                        counter += 1
                if counter == 4:
                    Win = True
                    return Win
    for i in range (4):
        for j in range(7):
            if Tableau[i+3][j]==c:
                counter = 1
                for k in range(3): #Vertical win
                    if Tableau[(i+3)-(k+1)][j]==c:
                        counter += 1
                if counter == 4:
                    Win = True
                    return Win
    Win = False
    return Win
            



#Boutons 
Bouton=tk.Button(racine, command=terrain_de_jeu  , text ="Generation de terrain de jeu" , font=("calibri" , "17") ) 
Bouton1=tk.Button(racine, command=player , text=("Quel joueur commence") , font=("Calibri" , "17"))



#positionnement 
canvas.grid()
Bouton.grid(row=0,column=1)
Bouton1.grid()


#Affichage de la fenetre 
racine.mainloop() 
