# Salman Nakhwa
# Start date 27 June 2024
# Project Hangman

from Hangman_Core import *
from tkinter import *

def Set_Level(a):

    if a == 1:
        Total_Tries = 9
    elif a == 2:
        Total_Tries = 6
    else:
        Total_Tries = 4

    StartGame(Total_Tries, root, my_movie)
    Difficulty_Menu.forget()


    


###################################################### Start ######################################################

my_movie = Choose_Movie()           # print(my_movie) # Cheat

root = Tk()
root.title("Hangman")
root.config(background="#aadfad")
root.geometry("1080x720+228+20")
    
Logo = PhotoImage(file="Pics/Logo.png")
root.iconphoto(True, Logo)
root.resizable(False, False)

Difficulty_Menu = Label(root)
Difficulty_Menu.config(background="#aadfad")

Above_Menu = Label (Difficulty_Menu, text="Select Difficulty", font=("Comic Sans MS", 35, 'bold')).pack()
Easy_Button = Button(Difficulty_Menu, text="Easy", font=("Ink Free", 30), relief=FLAT, command=lambda: Set_Level(1)).pack(fill=BOTH, expand=True)
Medium_Button = Button(Difficulty_Menu, text="Medium", font=("Ink Free", 30), relief=FLAT, command=lambda: Set_Level(2)).pack(fill=BOTH, expand=True)
Hard_Button = Button(Difficulty_Menu, text="Hard", font=("Ink Free", 30), relief=FLAT, command=lambda: Set_Level(3)).pack(fill=BOTH, expand=True)
Difficulty_Menu.pack()


root.mainloop()
