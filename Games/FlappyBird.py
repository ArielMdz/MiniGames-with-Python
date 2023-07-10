#Imports the needed modules
import random
import pygame
from pygame.locals import *

#Constants
WINDOW_W = 800
WINDOW_H = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)
GREEN_T = (77, 170, 45)
BLUE_C = (27, 234, 241)
FLAPPY_W = 50
FLAPPY_H = 50

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
    
    def hit(self, flappy):
        
        global score, game_over
        
        if((flappy.x + flappy.width > self.x)
            and (flappy.x < self.x + self.width)
            and (flappy.y < self.height
                or flappy.y + flappy.height > self.height + 200)):
            
            game_over = True
            
        if((flappy.x + flappy.width > self.x)
            and (flappy.x < self.x + self.width)
            and (flappy.y > self.height
                or flappy.y + flappy.height < self.height + 200)):
            
            score += 1


class Flappy: #Defines the Flappy class
    
    def __init__(self, image_file): #Initializes the Flappy Bird
        imageF = pygame.image.load(image_file)
        self.image = pygame.transform.scale(imageF, (FLAPPY_W, FLAPPY_H))
        
        self.width, self.height = self.image.get_size()
        
        #Position
        self.x = 250 - int(self.width / 2)
        self.y = int(WINDOW_H / 2)
        
        self.dir_y = 0
        
    def move(self): #Function that moves the bird up or down
        self.y += self.dir_y
        
        #print("Flappy X: ", self.x)
        #print("Flappy Y: ", self.y)
        
    def out(self):
        if ((self.y >= WINDOW_H)
            or self.y <= 0):
            
            pygame.quit()


def game_over_screen(letters, window):
    
    textg1 = letters.render("GAME OVER", True, (BLACK))
    textg2 = letters.render("Final score: " + str(round(score / 24)), True, (BLACK))
    
    window.blit(textg1, ((WINDOW_W / 2) - (textg1.get_width() / 2), (WINDOW_H / 2) - 50))
    window.blit(textg2, ((WINDOW_W / 2) - (textg2.get_width() / 2), WINDOW_H / 2))


def main(): #MAIN FUNCTION
    
    global score, game_over
    
    pygame.init()
    
    window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    pygame.display.set_caption("Flappy Bird")
    letters = pygame.font.Font(None, 50)
    
    gameIcon = pygame.image.load('.\Images\\flappy_bird.png')
    pygame.display.set_icon(gameIcon)

    flappy = Flappy(".\images\\flappy_bird.png")
    
    speed = 5
    score = 0
    
    tubes = []
    
    for i in range(0, 3):
        tubes.append(Tubes(random.randint(10, 390), (WINDOW_W + i*291)))
        
    playing = True
    game_over = False
    
    while playing:
        
        flappy.move()
        flappy.out()
        
        window.fill(BLUE_C)
        window.blit(flappy.image, (flappy.x, flappy.y))
        
        text = f"SCORE: {round(score / 24)}"
        scoreboard = letters.render(text, False, BLACK)
        window.blit(scoreboard, ((WINDOW_W / 2) - (letters.size(text)[0] / 2), 60))
        
        if not game_over:
            for tube in range(0, 3):
                
                if (tubes[tube].hit(flappy)):
                    game_over = True
                
                tubes[tube].move(speed)
                tubes[tube].draw(window)
                
                if tubes[tube].x < -75:
                    tubes[tube] = Tubes(random.randint(10, 400), WINDOW_W)
                
            for event in pygame.event.get():
                if event.type == QUIT:
                    playing = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        flappy.dir_y = -7
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        flappy.dir_y = +7
        
        
        if game_over:
            
            game_over_screen(letters, window)
            pygame.display.flip()
            
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        playing = False

                if not playing:
                    break
            
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
        
    pygame.quit()
    return True
        
#if __name__ == "__main__": #Executes the main function
#    main()