#!/usr/bin/python
import random
import tkinter as tk

from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk,Image  



while True:
    print(" Enter \n 1 Rock\n 2 Paper\n 3 Scissors")
    UsersChoice = int(input("Enter a number"))
    UsersChoice = UsersChoice%4
    ComputersChoice = random.randint(1,3)
    print(ComputersChoice)

    if( UsersChoice == ComputersChoice ):
        print("TIE")
    elif( (UsersChoice == 1 and ComputersChoice == 3) or (UsersChoice == 2 and ComputersChoice == 1) or (UsersChoice == 3 and ComputersChoice == 2)):
        print("You won")
    else:
        print("You lost")
    Deci = input("Do you want to continue Y/N")    
    if( Deci == "N" or Deci == "n" ):
        break


root = tk.Tk()
Rock = PhotoImage( file = r"Rock.png")
Paper = PhotoImage( file = r"Paper.png")
Scissors = PhotoImage( file = r"Scissors.png")
Rock1 = Rock.subsample(20, 20)
Paper1 = Paper.subsample(20, 20)
Scissors1 = Scissors.subsample(20, 20)
Button(root, text = 'Rock', image = Rock1, compound = LEFT).pack(side = LEFT)
Button(root, text = 'Paper', image = Paper1, compound = LEFT).pack(side = LEFT)
Button(root, text = 'Scissors', image = Scissors1, compound = LEFT).pack(side = LEFT)
root.mainloop()
