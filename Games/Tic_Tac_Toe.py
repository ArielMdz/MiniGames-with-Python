'''Este programa consistira en realizar el clascio juego de Tic-Tac-Toe'''
import pygame

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

        pygame.display.flip()

    pygame.quit()