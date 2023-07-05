'''! Este programa consiste en una interfaz grafica principal de mini juegos, se encargara de dar acceso a cada uno
de los distintos juegos mediante botones, cada boton se encargara de llamar a los distintos juegos por medio de modulos
indepedientes teniendo cada programa su propio codigo aislado'''
from tkinter import *           #Se importo toda la libreria  de Tkinter
from Games import Snake
from Games import PingPong
from Games import Tic_Tac_Toe

def mainWindow():
    global windowMain
    windowMain = Tk()
    windowMain.geometry("500x250")
    windowMain.configure(background = "black")
    windowMain.title("Mini Games")

    # Establecer ícono de la ventana
    icono = PhotoImage(file = "Icon.png")
    windowMain.iconphoto(True, icono)
    
    Label(windowMain, text="Welcome to MiniGames!", fg = "white", bg= "black", justify = "center", font=("Arial", 16)).pack(anchor = CENTER)

    snake_photo = PhotoImage(file = 'Snake.png')
    snake_image = snake_photo.subsample(30, 30)
    Button(windowMain, text = "Snake Game", font = ("segoe print", 14), image = snake_image, compound = LEFT, bg = "green", fg = "white", width = 250, height = 100, command = game1).pack(side = LEFT)

    pong_photo = PhotoImage(file = 'Pong.png')
    pong_image = pong_photo.subsample(3, 3)
    Button(windowMain, text = "Ping Pong", font = ("segoe print", 14), image = pong_image, compound = LEFT, bg = "green", fg = "white", width = 250, height = 100, command = game2).pack(side = RIGHT)
    
    windowMain.mainloop()

def game1():
    while True:
        windowMain.withdraw()
        if Snake.start_game():
            break
    windowMain.iconify()
    windowMain.deiconify()

def game2():
    while True:
        windowMain.withdraw()
        if PingPong.main():
            break
    windowMain.iconify()
    windowMain.deiconify()

if __name__ == '__main__':
    mainWindow()