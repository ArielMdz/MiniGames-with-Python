'''Este programa consistira en realizar el clascio juego de Snake'''
import pygame
import random

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)

def init_game():
    #varaiables de posicion y control de movimiento de la serpiente
    global move, snake_x_coor, snake_y_coor, tail
    move = 'None'
    snake_x_coor = 350
    snake_y_coor = 350
    tail = []

    #variables de posicion de la comida, esta tomara un valor aleatorio dentro del area de juego
    global food_x_coor, food_y_coor
    food_x_coor = random.randrange(10, 690, 10)
    food_y_coor = random.randrange(110, 590, 10)

    #Variables de puntaje y velocidad
    global score, speed
    score = 0
    speed = 5

def start_game():
    global move, snake_x_coor, snake_y_coor, tail
    global food_x_coor, food_y_coor, score, speed
    init_game()

    pygame.init()                               #Se crea la ventana 
    pygame.display.set_caption('Snake Game')    #Se asigna un titulo

    gameIcon = pygame.image.load('.\Images\Snake.png')
    pygame.display.set_icon(gameIcon)

    screen = pygame.display.set_mode([700, 600])    #Se define tamaño de ventana
    clock = pygame.time.Clock()                     #Se declara un reloj para los fps

    font = pygame.font.SysFont("segoe print", 40)
    font2 = pygame.font.SysFont("arial black", 20)
    text = font.render("Snake Game", True, WHITE)
    text_end = font2.render("Game over! Press 'R' for repeat or 'Q' for Quit", True, WHITE)

    game_over = True
    game = True
    while game:
        #Eventos que se encargan de cerrar el juego y controlar los movimientos por teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           #Evento de fin de Juego oprimiendo X
                game = False
            
            #Eventos de teclado, se asignan eventos para las flechas para que snake pueda moverse
            if event.type == pygame.KEYDOWN:
                if move == 'RIGHT' or move == 'LEFT' or move == 'None':
                    if event.key == pygame.K_UP:
                        move = 'UP'
                    if event.key == pygame.K_DOWN:
                        move = 'DOWN'
                if move == 'UP' or move == 'DOWN' or move == 'None':        
                    if event.key == pygame.K_RIGHT:
                        move = 'RIGHT'
                    if event.key == pygame.K_LEFT:
                        move = 'LEFT'
                if event.key == pygame.K_r:
                    game_over = True
                    init_game()
                if event.key == pygame.K_q:
                    game = False
        
        if game_over:
            #Movimiento de la cola
            i = len(tail) - 1
            if i >= 0: 
                while not i == 0:
                    tail[i] = tail[i - 1]
                    i -= 1
                tail[0] = (snake_x_coor, snake_y_coor)
                
            #Condiciones de movimiento de snake, este se seguira moviendo en una direccion hasta que se presione otra tecla
            if move == 'UP':
                snake_y_coor -= 10
            elif move == 'DOWN':
                snake_y_coor += 10
            elif move == 'RIGHT':
                snake_x_coor += 10
            elif move == 'LEFT':
                snake_x_coor -= 10

        #Si snake se sale de los limites el juego termina
        if snake_x_coor < 10 or snake_x_coor >= 690 or snake_y_coor < 110 or snake_y_coor >= 590 or (snake_x_coor, snake_y_coor) in tail:
            move = 'None'
            game_over = False

        #Si snake coicide con las coordenadas de foos se sumara un punto, se aumentara la velocidad(limitada a 60) y se asignara otra food
        if food_x_coor == snake_x_coor and food_y_coor == snake_y_coor:
            score += 1
            tail.append((food_x_coor, food_y_coor))
            food_x_coor = random.randrange(10, 690, 10)
            food_y_coor = random.randrange(110, 590, 10)
            if speed < 60:
                speed += 1
            else:
                speed = 60
        
        text_score = font2.render("Score: " + str(score), True, WHITE)
        text_speed = font2.render("Speed: " + str(speed), True, WHITE)

        #Area de juego
        screen.fill(BLACK)
        pygame.draw.rect(screen, DARK_GREEN, (10, 110, 680, 480))
        
        #Zona de Dibujo
        pygame.draw.rect(screen, WHITE, (snake_x_coor, snake_y_coor, 10, 10))
        for i in range(0, len(tail)):
            pygame.draw.rect(screen, WHITE, (tail[i][0], tail[i][1], 10, 10))
        pygame.draw.rect(screen, RED, (food_x_coor, food_y_coor, 10, 10))
        screen.blit(text, (225, 10))
        screen.blit(text_score, (10, 20))
        screen.blit(text_speed, (10, 60))
        if not game_over:
            screen.blit(text_end, (100, 300))
        
        pygame.display.flip()
        clock.tick(speed)
    
    pygame.quit()
    return True

#start_game()