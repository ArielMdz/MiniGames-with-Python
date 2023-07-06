import pygame
import copy

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

SIZE_X = (1001, 101)
SIZE_Y = (601, 51)

def init_game():
    global cells, cells_before, cells_neighboring, pos_game
    cells = [[0 for i in range(0, SIZE_Y[1])] for j in range(0, SIZE_X[1])] 
    cells_before = [[0 for i in range(0, SIZE_Y[1])] for j in range(0, SIZE_X[1])] 
    cells_neighboring = [[0 for i in range(0, SIZE_Y[1])] for j in range(0, SIZE_X[1])]
    pos_game = [SIZE_X[1]-1, SIZE_Y[1]-1]

def cursor_mouse(x, y):
    if y > 100 and y < SIZE_Y[0]-1 and x > 0 and x < SIZE_X[0]-1:
        return [(int(x/10)), (int((y - 100)/10))]
    else: 
        return [SIZE_X[1]-1, SIZE_Y[1]-1]
    

def start_game():
    #Declaracion de varaibles 
    global cells, cells_before, cells_neighboring, pos_game
    init_game()

    pygame.init()                               #Se crea la ventana 
    pygame.display.set_caption('Game of Life')    #Se asigna un titulo
    gameIcon = pygame.image.load('.\Images\Life.png')
    pygame.display.set_icon(gameIcon)

    screen = pygame.display.set_mode([SIZE_X[0], SIZE_Y[0]])    #Se define tamaño de ventana
    clock = pygame.time.Clock()                     #Se declara un reloj para los fps

    font = pygame.font.SysFont("segoe print", 40)
    text = font.render("Game of Life", True, WHITE)

    font2 = pygame.font.SysFont("arial black", 16)
    text_P =font2.render("Press 'P' for Play/Pause", True, WHITE)
    text_R =font2.render("Press 'R' for Reset", True, WHITE)

    game = True
    play = False
    while game:
        #Eventos que se encargan de cerrar el juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            #Evento de poscion de mouse
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
                pos_game = cursor_mouse(pos[0], pos[1])
            #Evento de click de boton
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                pos_life = cursor_mouse(pos[0], pos[1])
                if cells[pos_life[0]][pos_life[1]] == 0 and not pos_life == [SIZE_X[1]-1, SIZE_Y[1]-1]:
                    cells[pos_life[0]][pos_life[1]] = 1
                elif not pos_life == [SIZE_X[1]-1, SIZE_Y[1]-1]:
                    cells[pos_life[0]][pos_life[1]] = 0
            #Eventos de teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    play = not play
                if event.key == pygame.K_r:
                    init_game()
        
        #Color de fondo, titulod y textos de juego
        screen.fill(BLACK)
        text_title = text.get_rect(center = (int(SIZE_X[0]/2), 50))
        screen.blit(text, text_title).center
        screen.blit(text_P, (750, 25))
        screen.blit(text_R, (750, 50))

        #Condicion de juego play o pausa
        if play:
            #Incializacion de variables para conteo de vecinos y copia de matriz de celulas anterior 
            cells_before = copy.deepcopy(cells)
            cells_neighboring = [[0 for i in range(0, SIZE_Y[1])] for j in range(0, SIZE_X[1])]
            #Ciclos para la modificacion de celulas
            for i in range(0, SIZE_X[1]-1):
                for j in range(0, SIZE_Y[1]-1):
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if SIZE_X[1]-1 > i+k and i+k >= 0 and SIZE_Y[1]-1 > j+l and j+l >= 0 and not k == l == 0:
                                cells_neighboring[i][j] += cells_before[i+k][j+l]
                    if (cells_neighboring[i][j] == 2 and cells[i][j] == 1) or cells_neighboring[i][j] == 3 :
                        cells[i][j] = 1
                    else:
                        cells[i][j] = 0
                
        #altera el valor de la celula sobre la que se encuentra el mouse
        if cells[pos_game[0]][pos_game[1]] == 0 and not pos_game == [SIZE_X[1]-1, SIZE_Y[1]-1]:
            cells[pos_game[0]][pos_game[1]] = 2
        
        #Imprime totas las celulas
        for column in range(0, SIZE_X[0]-1, 10):
            for row in range(100, SIZE_Y[0]-1, 10):
                x = int(column / 10)
                y = int((row - 100) / 10)
                if cells[x][y] == 0:
                    pygame.draw.rect(screen, GRAY, (column, row, 9, 9))
                elif cells[x][y] == 1:
                    pygame.draw.rect(screen, GREEN, (column, row, 9, 9))
                elif cells[x][y] == 2:
                    pygame.draw.rect(screen, YELLOW, (column, row, 9, 9))
                    cells[x][y] = 0

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()
    return True

#if __name__ == '__main__':
#    start_game()
    