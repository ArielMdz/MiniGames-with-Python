'''Este programa consistira en realizar el clascio juego de Tic-Tac-Toe'''
import pygame
WHITE = (255, 255, 255)


def start_game():
    pygame.init()
    pygame.display.set_caption('Tic-Tac-Toe')

    screen = pygame.display.set_mode([500, 500])

    running = True
    while running:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        pygame.draw.line(screen, WHITE, [200, 150], [200, 450], 5)
        pygame.draw.line(screen, WHITE, [300, 150], [300, 450], 5)
        pygame.draw.line(screen, WHITE, [100, 250], [400, 250], 5)
        pygame.draw.line(screen, WHITE, [100, 350], [400, 350], 5)

        pygame.display.flip()

    pygame.quit()
