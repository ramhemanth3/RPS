#!/usr/bin/python
import random
import tkinter as tk

from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk,Image  
from tkinter import messagebox


def fun( buttonstatus):
    UsersChoice = buttonstatus%4
    ComputersChoice = random.randint(1,3)


    if( UsersChoice == ComputersChoice ):
        return "TIE"
    elif( (UsersChoice == 1 and ComputersChoice == 3) or (UsersChoice == 2 and ComputersChoice == 1) or (UsersChoice == 3 and ComputersChoice == 2)):
        return "You won"
    else:
        return "You lost"
 
    

root = tk.Tk()

def ROCK():
    showMsg(1)
    
def PAPER():
    showMsg(2)

def SCISSORS():
    showMsg(3)    


def showMsg(buttonstatus):
    text = fun(buttonstatus)
    #text = "heyy"
    messagebox.showinfo('Message', text)
 
Rock = PhotoImage( file = r"Rock.png")
Paper = PhotoImage( file = r"Paper.png")
Scissors = PhotoImage( file = r"Scissors.png")
Rock1 = Rock.subsample(20, 20)
Paper1 = Paper.subsample(20, 20)
Scissors1 = Scissors.subsample(20, 20)
rockButt = Button(root, text = 'Rock', image = Rock1, compound = LEFT, command = ROCK).pack(side = LEFT)
paperButt = Button(root, text = 'Paper', image = Paper1, compound = LEFT, command = PAPER).pack(side = LEFT)
scissorsButt = Button(root, text = 'Scissors', image = Scissors1, compound = LEFT, command = SCISSORS).pack(side = LEFT)

root.mainloop()