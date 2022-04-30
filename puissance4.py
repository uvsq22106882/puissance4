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
#interface 
racine=tk.Tk()
racine.title("puissance 4")
canvas=tk.Canvas(racine, bg="blue" , height=500 , width=500)
#Fonctions 
def terrain_de_jeu():
    global n, z
    for i in range(7):
        for j in range(7):
            canvas.create_oval(n,z,n+70,z+70, fill="white" , outline="black")
            n=n+70
        z=z+70
        n=5

def player():
    c=rd.randint(0,10)
    if c%2==0 :
        canvas.create_text(250 , 250 , text="le joueur 1 commence " , fill="black" , font=("calibri","22")) 
        
    else : 
        canvas.create_text(250, 250 , text ="le joueur 2 commence " , fill="black" , font=("calibri" , "22"))
        
#def annuler le dernier coup 
#def winner():
    #global x , y
    #if ..... :
        #y=y+1
        #canvas.create_text(racine , text=("joueur 1 a gagné la partie pour la ", y ,"fois"))
    #elif ..... : 
        #x=x+1
        #canvas.create_text(racine , text=("joueur 2 a gagné la partie pour la " , x , "fois "))
    #else :
        #canvas.create_text(racine , text=("match nul ") )

#def affichage_du_score():
    #canvas.create_text


 
#Bouttons 
Bouton=tk.Button(racine, command=terrain_de_jeu  , text ="Generation de terrain de jeu" , font=("calibri" , "17") )    
Bouton1=tk.Button(racine, command=player , text=("Quel joueur commence") , font=("Calibri" , "17"))
Bouton2= tk.Button(racine, command="...."   )


#positionnement 
canvas.grid()
Bouton.grid(row=0,column=1)
Bouton1.grid()
Bouton2.grid()

#Affichage de la fenetre 
racine.mainloop() 



