'''Este programa consistira en realizar el clascio juego de Tic-Tac-Toe'''
import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#Funcion de posicionamieno de clic de mouse
def click_mouse(x, y):
    if x > 100 and x <= 200:
        postion = 0
    elif x > 200 and x <= 300:
        postion = 1
    elif x > 300 and x <= 400:
        postion = 2
    else:
        return 9
    
    if y > 150 and y <= 250:
        pass
    elif y > 250 and y <= 350:
        postion += 3
    elif y > 350 and y <= 450:
        postion += 6
    else:
        return 9
    
    return postion

#Funcionn que se encarga de verificar si existe un ganador
def win_game(TTT):
    for gamer in range(1, 3):
        if TTT[0] == gamer and ((TTT[1] == TTT[2] == gamer) or (TTT[3] == TTT[6] == gamer) or (TTT[4] == TTT[8] == gamer)) or (TTT[4] == gamer and 
        ((TTT[1] == TTT[7] == gamer) or (TTT[3] == TTT[5] == gamer))) or (TTT[8] == gamer and ((TTT[2] == TTT[5] == gamer) or 
        (TTT[6] == TTT[7] == gamer))) or TTT[2] == TTT[4] == TTT[6] == gamer:
            return gamer

    return 0
            

def start_game():
    #Se establecen posiciones de X y O, los valores de sus posciones y varaible de ganador
    position = [(110, 140), (215, 140), (320, 140), (110, 240), (215, 240), (320, 240), (110, 340), (215, 340), (320, 340)]
    TTT = [0] * 10
    winner = 0
    
    #Se inicializa la pantalla con titulo, nombre e icono
    pygame.init()
    pygame.display.set_caption('Tic-Tac-Toe')
    screen = pygame.display.set_mode([500, 500])
    gameIcon = pygame.image.load('TTT.png')
    pygame.display.set_icon(gameIcon)

    #Se establecen distintas fuentes y textos
    font = pygame.font.SysFont("segoe print", 36)
    text_title = font.render("TIC-TAC-TOE", True, WHITE)

    font2 = pygame.font.SysFont("arial black", 20)
    text_player1 = font2.render("Turn Player 1: X", True, WHITE)
    text_player2 = font2.render("Turn Player 2: O", True, WHITE)
    text_end =font2.render("Press 'R' for repeat or 'Q' for Quit", True, WHITE)

    font3 = pygame.font.SysFont("arial black", 80)
    text_x = font3.render("X", True, RED)
    text_o = font3.render("O", True, BLUE)
    
    #Se asigna un primer turno aleatorio
    turn = random.randrange(1, 3, 1)
    
    #Se inicializa el ciclo
    game_over = True
    game = True
    while game:
        #Eventos que se encargan de cerrar el juego, control por mouse y control de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

            #Eventos de poscisionamiento de mouse
            if event.type == pygame.MOUSEBUTTONDOWN and game_over:
                pos = event.pos
                pos_game = click_mouse(pos[0], pos[1])
                if TTT[pos_game] == 0 and not pos_game == 9:
                    TTT[pos_game] = turn
                    if turn == 1:
                        turn = 2
                    else:
                        turn = 1

            #Eventos de teclado para reset y quit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = True
                    TTT = [0] * 10
                    winner = 0
                if event.key == pygame.K_q:
                    game = False

        #Color de fondo y texto de titulo de juego
        screen.fill(BLACK)
        screen.blit(text_title, (125, 10))
        
        #Zona de dibujo del Juego #
        pygame.draw.line(screen, WHITE, [200, 150], [200, 450], 5)
        pygame.draw.line(screen, WHITE, [300, 150], [300, 450], 5)
        pygame.draw.line(screen, WHITE, [100, 250], [400, 250], 5)
        pygame.draw.line(screen, WHITE, [100, 350], [400, 350], 5)
        
        for i in range(0, 9):
            if TTT[i] == 1:
                screen.blit(text_x, position[i])
            elif TTT[i] == 2:
                screen.blit(text_o, position[i])
        
        #Ciclo de verificacion de espacios disponibles 
        sum = 0
        for i in TTT:
            if not i == 0:
                sum += 1

        #Verificacion y condiciones de ganador
        winner = win_game(TTT)
        if not winner == 0:
            text_win = font2.render("Player winner " + str(winner), True, WHITE)
            screen.blit(text_win, (170, 460))
            game_over = False
        #Condicion de empate
        elif sum == 9:
            text_tie = font2.render("It's a tie", True, WHITE)
            screen.blit(text_tie, (205, 460))
            game_over = False
        #Cambio de turno de jugador
        else:
            if turn == 1:
                screen.blit(text_player1, (10, 90))
            elif turn == 2:
                screen.blit(text_player2, (300, 90))

        #Mensaje de fin de juego
        if not game_over:
            screen.blit(text_end, (60, 80))

        pygame.display.flip()

    pygame.quit()
    return True

#start_game()