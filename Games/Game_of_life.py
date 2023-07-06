import pygame

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)


def cursor_mouse(x, y):
    if y > 100 and y < 600 and x > 0 and x < 500:
        return [(int(x/10)), (int((y - 100)/10))]
    else: 
        return [50, 50]
    

def start_game():
    #Declaracion de varaibles 
    cells = [[0 for i in range(0, 51)] for j in range(0, 51)]
    cells_before = [[0 for i in range(0, 51)] for j in range(0, 51)]
    pos_game = [50, 50]
    print(pos_game[0], pos_game[1])
    pygame.init()                               #Se crea la ventana 
    pygame.display.set_caption('Snake Game')    #Se asigna un titulo

    screen = pygame.display.set_mode([501, 601])    #Se define tamaño de ventana
    clock = pygame.time.Clock()                     #Se declara un reloj para los fps

    font = pygame.font.SysFont("segoe print", 40)
    text = font.render("Game of Life", True, WHITE)

    game = True
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
                if cells[pos_life[0]][pos_life[1]] == 0 and not pos_life == [50, 50]:
                    cells[pos_life[0]][pos_life[1]] = 1
                elif not pos_life == [50, 50]:
                    cells[pos_life[0]][pos_life[1]] = 0
        
        #color y textos de la interfaz
        screen.fill(BLACK)
        screen.blit(text, (110, 10))

        #altera el valor de la celula sobre la que se encuentra el mouse
        if cells[pos_game[0]][pos_game[1]] == 0 and not pos_game == [50, 50]:
            cells[pos_game[0]][pos_game[1]] = 2
        
        #Imprime totas las celulas
        for column in range(0, 500, 10):
            for row in range(100, 600, 10):
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
        clock.tick(15)

    pygame.quit()

if __name__ == '__main__':
    start_game()
    