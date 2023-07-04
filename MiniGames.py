'''! Este programa consiste en una interfaz grafica principal de mini juegos, se encargara de dar acceso a cada uno
de los distintos juegos mediante botones, cada boton se encargara de llamar a los distintos juegos por medio de modulos
indepedientes teniendo cada programa su propio codigo aislado'''
from tkinter import *           #Se importo toda la libreria  de Tkinter
from Games import Snake
from Games import Tic_Tac_Toe

def mainWindow():
    global windowMain
    windowMain = Tk()
    windowMain.geometry("500x250")
    windowMain.configure(background = "black")
    windowMain.title("Mini Games")

    Label(windowMain, text="Welcome to MiniGames!", fg = "white", bg= "black", justify = "center", font=("Arial", 16)).pack(anchor = CENTER)

    #snake_photo = PhotoImage(file = r"Images/Snake.png")
    Button(windowMain, text = "Snake Game", bg = "green", fg = "white", width = 30, height = 5, command = game1).pack(side = LEFT)

    Button(windowMain, text = "Game 2", bg = "green", fg = "white", width = 30, height = 5, command = game2).pack(side = RIGHT)
    
    windowMain.mainloop()

def game1():
    while True:
        windowMain.withdraw()
        if Snake.start_game():
            break
    windowMain.iconify()
    windowMain.deiconify()

def game2():
    Tic_Tac_Toe.start_game()

if __name__ == '__main__':
    mainWindow()