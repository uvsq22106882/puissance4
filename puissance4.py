#############################
#GROUPE TD 3 
#BOUDINAR LOUNES 22106882
#SUBRAMANIAM SUYAN 22107171 
#SAMBE Momar 22000621

#https://github.com/uvsq22106882/puissance4.git

#import 

import tkinter as tk   #libraire interface graphique 
import random as rd    #libraire aléatoire 
from random import randint
import pickle as pc     #libraire pour sauvegarde 

#initialisation des variables 

#valeur remise à 0
x=0
y=0
d=0
cpt=0
total=0
Tableau1=[]

#Booléen 
t=True
l=True

#variable global 
c=rd.randint(1,2)
n=5
z=105
N=8

#interface 

racine=tk.Tk()
racine.title("puissance 4")
canvas=tk.Canvas(racine, bg="blue" , height=800 , width=700)

#Fonctions 

def terrain_de_jeu():  
    "generation du terrain de jeu une grille a 49 cercles"
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
    "quel joueur commence" 
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

def Colonnes(xclic):    
    "Définir dans quelle colonne est le clic"
    colonne=(xclic)//(100) 
    return colonne

def Lignes(colonne):
    "Vérifier si les jetons sont déjà présents dans la colonne pour choisir la ligne"
    for i in range(7):        
        p=6-i
        if Tableau[p][colonne]==0:
            ligne=p
            break
        else:
            p=p-1
    return ligne

def jeton (event): 
    "création des jetons dés le clic sur la case "
    global Tableau 
    global c , total , x, y
    xclic,yclic=event.x , event.y
    if 0<xclic<700 and 0<yclic<700: #Vérifier que le clic est dans le tableau
        colonne=Colonnes(xclic)
        ligne=Lignes(colonne)
        if c==1: #tour joueur rouge
            canvas.create_oval(colonne*100+100,ligne*100+110,colonne*100+10,ligne*100+200, fill='red') #Placement du jeton au milieu de la case
            Tableau[ligne][colonne]=1      #Définir que cette case est rouge dans le tableau
            Win = WinCondition()
            total=total+1
            c=2
            print("Au tour du joueur 2")
        elif c==2: #Tour du joueur jaune
            canvas.create_oval(colonne*100+100,ligne*100+110,colonne*100+10,ligne*100+200, fill='yellow') #Placement du jeton au milieu de la case
            Tableau[ligne][colonne]=2
            Win = WinCondition()
            total=total+1
            c=1
            print("Au tour du joueur 1")
    if total == 1:
        canvas.create_rectangle(0,0,750,100, fill="grey")   #pour afficher du text , le résultat 
    if Win == True:
        if c==1:
            canvas.create_text(350 , 50 , text ="Joueur 2 (Jaune) gagne!" , fill="black" , font=("calibri","22"))
            return
        else:
            canvas.create_text(350 , 50 , text ="Joueur 1 (Rouge) gagne!" , fill="black" , font=("calibri","22"))
            return
    elif Win==False and total==49:
        canvas.create_text(350,50, text="égalité" , fill="black" , font=("calibri " , "22"))
canvas.bind("<Button-1>", jeton)


def WinCondition(): 
    "Vérifie l'alligenement de 4 jetons de la meme couleur horizontalement , verticalement et en diagonale "
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


            
def annuler():  
    "annuler le dernier coup joué "
    canvas.after_cancel("<Button-1>", jeton)

 
def Save():
    "sauvegarde du jeu en cours "
    fichier= open("sauvegarde","w")
    pc.dump(Tableau1, fichier)
    fichier.close()

def Load():
    "reprendre la partie laissé  "
    global Tableau1 
    Tableau2=[]
    fichier= open("sauvegarde", "r") 
    pc.load(fichier)
    fichier.close()
    for line in fichier :
        Tableau2.append(line)
    Tableau1=Tableau2

# -----------------------------------------------------------------------------------



def partie_():
    "montrer le nombre de fois que chaqu'un a gagné "
    global cpt 
    if total%4==0 and c==1 and Win==True:
        cpt=cpt+1
        print("le nombre de partie gagné par le joueur 1 est", cpt)
    elif total%4==0 and c==2 and Win==True: 
        cpt=cpt+1
        print("le nombre de partie gagné par le joueur 2 est", cpt)   



# --------------------------------------------------------------------------------------------

#Boutons 

Bouton=tk.Button(racine, command=terrain_de_jeu  , text ="Generation de terrain de jeu" , font=("calibri" , "17") ) 
Bouton1=tk.Button(racine, command=player , text=("Quel joueur commence") , font=("Calibri" , "17"))
Bouton2=tk.Button(racine, command=annuler , text=("Annuler le coup") , font=("calibri","17"))
Bouton3=tk.Button(racine,command=Save ,  text="Sauvegarde" , font=("calibri","22"))
Bouton4=tk.Button(racine, command=Load , text="telecharge" , font=("calibri" , "22"))



#------------------------------------------------------------

#positionnement 

canvas.grid()
Bouton.grid(row=0,column=1)
Bouton1.grid(row=0 , column=2)
Bouton2.grid(row=1, column=1)
Bouton3.grid()
Bouton4.grid(row=1, column=2)


#Affichage de la fenetre 

racine.mainloop() 
