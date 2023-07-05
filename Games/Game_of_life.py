import pygame

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)


def cursor_mouse(x, y):
    if y > 100 and y < 601 and x > 0 and x < 501:
        return int(x/10) + (50 * int((y - 100)/10))
    else: 
        return 3000
    

def start_game():
    #init_game()
    cells = [0] * 3001
    cells_before = [0] * 3001

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

            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
                pos_game = cursor_mouse(pos[0], pos[1])

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos= event.pos
                pos_life = cursor_mouse(pos[0], pos[1])
                if cells[pos_life] == 0 and not pos_life == 3000:
                    cells[pos_life] = 1
                elif not pos_life == 3000:
                    cells[pos_life] = 0
                
        if cells[pos_game] == 0 and not pos_game == 3000:
            cells[pos_game] = 2
        screen.fill(BLACK)
        screen.blit(text, (110, 10))
        
        for i in range(0, 500, 10):
            for j in range(100, 600, 10):
                index = int(i/10 + (50 * (j-100)/10))
                if cells[index] == 0:
                    pygame.draw.rect(screen, GRAY, (i, j, 9, 9))
                elif cells[index] == 1:
                    pygame.draw.rect(screen, GREEN, (i, j, 9, 9))
                else:
                    pygame.draw.rect(screen, YELLOW, (i, j, 9, 9))
                    cells[index] = 0
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    start_game()
    