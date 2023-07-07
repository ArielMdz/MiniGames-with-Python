#Imports the needed modules
import random
import pygame
from pygame.locals import *

#Constants
WINDOW_W = 800
WINDOW_H = 600
FPS = 120
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)
GREEN_T = (77, 170, 45)
BLUE_C = (27, 234, 241)
FLAPPY_W = 75
FLAPPY_H = 75


class Tubes: #Defines the tubes class
    
    def __init__(self, height, x):
        self.color = GREEN_T
        self.width = 75
        self.height = height
        self.x = x
        
    def move(self, speed):
        self.x -= speed
        
    def draw(self, window):
            #pygame.draw.rect(ventana, color_rectangulo, (x_rectangulo, y_rectangulo, ancho_rectangulo, alto_rectangulo))
            pygame.draw.rect(window, GREEN_T, (self.x, 0, self.width, self.height))
            pygame.draw.rect(window, GREEN_T, (self.x, self.height + 200, self.width, 450 - self.height))
            
            


class Flappy: #Defines the Flappy class
    
    def __init__(self, image_file): #Initializes the Flappy Bird
        imageF = pygame.image.load(image_file)
        self.image = pygame.transform.scale(imageF, (FLAPPY_W, FLAPPY_H))
        
        self.width, self.height = self.image.get_size()
        
        #Position
        self.x = 250 - (self.width / 2)
        self.y = (WINDOW_H / 2) 
        
        self.dir_y = 0
        
    def move(self): #Function that moves the bird up or down
        self.y += self.dir_y
        
    def out(self):
        if ((self.y >= WINDOW_H)
            or self.y <= 0):
            
            pygame.quit()



def main(): #MAIN FUNCTION
    
    pygame.init()
    
    window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    pygame.display.set_caption("Flappy Bird")
    letters = pygame.font.Font(None, 50)
    
    flappy = Flappy("./Images/flappy_bird.png")
    
    speed = 2

    tubes = []
    
    for i in range(0, 3):
        tubes.append(Tubes(random.randint(10, 390), (WINDOW_W + i*291)))
        
    playing = True
    
    while playing:
        
        flappy.move()
        flappy.out()
        
        window.fill(BLUE_C)
        window.blit(flappy.image, (flappy.x, flappy.y))
        
        for tube in range(0, 3):
            tubes[tube].move(speed)
            tubes[tube].draw(window)
            if tubes[tube].x <= -75:
                tubes[tube] = Tubes(random.randint(10, 400), WINDOW_W)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    flappy.dir_y = -2
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    flappy.dir_y = +2
        
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
        
    pygame.quit()
        
if __name__ == "__main__": #Executes the main function
    main()