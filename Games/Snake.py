'''Este programa consistira en realizar el clascio juego de Snake'''
import pygame
import random
#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)


def start_game():
    #varaiables de posicion y control de movimiento de la serpiente
    move = 'None'
    snake_x_coor = 350
    snake_y_coor = 350

    #variables de posicion de la comida, esta tomara un valor aleatorio dentro del area de juego
    food_x_coor = random.randrange(10, 690, 10)
    food_y_coor = random.randrange(110, 590, 10)

    #Variables de puntaje y velocidad
    score = 0
    speed = 5
    
    pygame.init()                       #Se crea la ventana 
    pygame.display.set_caption('Snake Game')    #Se asigna un titulo

    screen = pygame.display.set_mode([700, 600])    #Se define tamaño de ventana
    clock = pygame.time.Clock()                     #Se declara un reloj para los fps

    game = True
    while game:
        #Eventos que se encargan de cerrar el juego y controlar los movimientos por teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           #Evento de fin de Juego oprimiendo X
                game = False
            
            #Eventos de teclado, se asignan eventos para las flechas para que snake pueda moverse
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move = 'UP'
                if event.key == pygame.K_DOWN:
                    move = 'DOWN'
                if event.key == pygame.K_RIGHT:
                    move = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    move = 'LEFT'
        
        #Condiciones de movimiento de snake, este se seguira moviendo en una direccion hasta que se presione otra tecla
        if move == 'UP':
            snake_y_coor -= 10
        elif move == 'DOWN':
            snake_y_coor += 10
        elif move == 'RIGHT':
            snake_x_coor += 10
        elif move == 'LEFT':
            snake_x_coor -= 10

        #Si snake coicide con las coordenadas de foos se sumara un punto, se aumentara la velocidad(limitada a 60) y se asignara otra food
        if food_x_coor == snake_x_coor and food_y_coor == snake_y_coor:
            score += 1
            food_x_coor = random.randrange(10, 690, 10)
            food_y_coor = random.randrange(110, 590, 10)
            if speed < 60:
                speed += 1
            else:
                speed = 60
        
        #Area de juego
        screen.fill(BLACK)
        pygame.draw.rect(screen, DARK_GREEN, (10, 110, 680, 480))
        
        #Si snake se sale de los limites el juego termina
        if snake_x_coor < 10 or snake_x_coor >= 690 or snake_y_coor < 110 or snake_y_coor >= 590:
            move = 'None'
            print("Game Over!")
            game = False
        
        #Zona de Dibujo
        snake = pygame.draw.rect(screen, WHITE, (snake_x_coor, snake_y_coor, 10, 10))
        food = pygame.draw.rect(screen, RED, (food_x_coor, food_y_coor, 10, 10))
            
        pygame.display.flip()
        clock.tick(speed)
    
    pygame.quit()
    return True

#start_game()