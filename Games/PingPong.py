#Imports the needed modules
import random
import pygame
from pygame.locals import QUIT

#Constants for the window size
WINDOW_W = 800 #Width
WINDOW_H = 600 #Height
FPS = 60 #Frames per second (refresh rate)
WHITE = (255, 255, 255) #Background color (Red, Green, Blue)
BLACK = (0, 0, 0) #Text color (Red, Green, Blue)
BALL_W = 20 #Ball width
BALL_H = 20 #Ball height
RACKET_W = 15 #Racket width
RACKET_H = 90 #Racket height

class PongBall: #Defines the class for the ball
    def __init__(self, image_file):
        #Class atributes
        
        #Image of the ball
        imageB = pygame.image.load(image_file)
        self.image = pygame.transform.scale(imageB, (BALL_W, BALL_H))
        
        #Ball dimensions
        self.width, self.height = self.image.get_size()
        
        #Ball position
        #This allow us to print the ball in the center, keeping in mind that we are using the superior left corner as the position
        self.x = (WINDOW_W / 2) - (self.width / 2)
        self.y = (WINDOW_H / 2) - (self.height / 2)
        
        #Movement direction, this determines the quantity of pixels that the ball will move
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])
        
        #Ball score for the player and the bot
        self.score = 0 #Saves the player score
        self.bot_score = 0 #Saves the bot score
    
    def move(self): #Function that determines the ball movement
        self.x += self.dir_x
        self.y += self.dir_y
        
    def bounce(self): #Function that determines the ball limits in the window and changes direction in the case the ball reachs the limits
        
        #Calls the reset function when the ball has trespassed the left or right limits
        if self.x <= 0:
            self.reset()
            self.bot_score += 1 #If the ball trespassed the left limit the bot scores 1
        
        if (self.x + self.width) >= WINDOW_W:
            self.reset()
            self.score += 1 #If the ball trespassed the right limit the player scores 1
        
        if self.y <= 0: #If the ball trespassed the upper or lower limit, bounces back
            self.dir_y = -self.dir_y
        
        if (self.y + self.height) >= WINDOW_H:
            self.dir_y = -self.dir_y
            
    def reset(self): #Function that checks if the ball has traspased the left and right limits
        self.x = (WINDOW_W / 2) - (self.width / 2)
        self.y = (WINDOW_H / 2) - (self.height / 2)
        
        #In case it does resets the ball to the center and with the contrary direction
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])   


class PongRacket: #Defines the class for the rackets
    def __init__(self):
        imageR = pygame.image.load("racket.png").convert_alpha()
        self.image = pygame.transform.scale(imageR, (RACKET_W, RACKET_H))
        #Class atributes
        
        #Racket dimensions
        self.width, self.height = self.image.get_size()
        
        #Racket position
        self.x = 0 #Centers the racket
        self.y = (WINDOW_H / 2) - (self.height / 2)
        
        #Racket direction
        self.dir_y = 0
        
    def move(self): #Function that determines and limits the racket movement to the window size
        self.y += self.dir_y
        
        if self.y <= 0: 
            self.y = 0
            
        if (self.y + self.height) >= WINDOW_H:
            self.y = WINDOW_H - self.height
            
    '''def move_bot(self, ball): #Function that determines the movement of the racket bot
        if (self.y > ball.y):
            self.dir_y = -5
        
        elif self.y < ball.y:
            self.dir_y = 5
            
        else:
            self.dir_y = 0
            
        self.y += self.dir_y'''
            
    def hit(self, ball): #Function that checks if the racket has hit the ball

        if((self.x >= 0 #Check if the ball hits in the top and bottom edges of the racket, if so, let the ball pass
            and self.y == 0
            and ball.x == 0
            and ball.y == 0)
            or
            (self.x == RACKET_W
            and self.y == RACKET_H
            and ball.x == 0
            and ball.y == 0)
        ):
            ball.dir_x = ball.dir_x

            
        if( #This conditional detects if the dimensions of the ball has hited in the dimensions of the racket from the left side
            (ball.x < (self.x + self.width))
            and (ball.x > self.x)
            and ((ball.y + ball.height) > self.y)
            and (ball.y < (self.y + self.height))
        ): 
            #If so, then changes the direction of the ball contrary to the racket it hited
            ball.dir_x = -ball.dir_x
            ball.x = (self.x + self.width)
            
        if( #This conditional detects if the dimensions of the ball has hited in the dimensions of the racket from the right side
            ((ball.x + ball.width) > self.x)
            and (ball.x < (self.x + self.width))
            and ((ball.y + ball.height) > self.y)
            and (ball.y < (self.y + self.height))
        ):
            #If so, then changes the direction of the ball contrary to the racket it hited
            ball.dir_x = -ball.dir_x
            ball.x = (self.x - ball.width)
            
    '''def hit_bot(self, ball): #Function that checks if the bot racket has hited the ball
        
        if((self.x >= 0 #Check if the ball hits in the top and bottom edges of the racket, if so, let the ball pass
            and self.y == 0
            and ball.x == 0
            and ball.y == 0)
            or
            (self.x == RACKET_W
            and self.y == RACKET_H
            and ball.x == 0
            and ball.y == 0)
        ):
            ball.dir_x = ball.dir_x
        
        if( #This conditional detects if the dimensions of the ball has hited in the dimensions of the racket from the right side
            ((ball.x + ball.width) > self.x)
            and (ball.x < (self.x + self.width))
            and ((ball.y + ball.height) > self.y)
            and (ball.y < (self.y + self.height))
        ):
            #If so, then changes the direction of the ball contrary to the racket it hited
            ball.dir_x = -ball.dir_x
            ball.x = (self.x - ball.width)'''


def main(): #Defines the main function
    
    #Pygame initialization
    pygame.init() 
    
    #Display surface and font initialization
    window = pygame.display.set_mode((WINDOW_W, WINDOW_H)) #Creates a window with the determined size
    pygame.display.set_caption("Pong") #Gives a name for the window
    letters = pygame.font.Font(None, 60)

    gameIcon = pygame.image.load('Pong.png')
    pygame.display.set_icon(gameIcon)

    ball = PongBall("green_ball.png") #Creates a variable of type PongBall
    
    racket1 = PongRacket() #Creates the left racket
    racket1.x = 60
    
    racket2 = PongRacket() #Creates the right racket
    racket2.x = WINDOW_W - 60 - racket2.width
    
    #Main loop
    playing = True #Bool variable that controls the loop
    
    while playing:
        
        ball.move() #Moves the ball
        ball.bounce() #Bounces the ball in the window limits
        racket1.move() #Moves the left racket
        racket2.move() #Moves the right ricket
        racket1.hit(ball) #Detects if the ball hits the left racket
        racket2.hit(ball) #Detects if the ball hits the right racket

        window.fill(WHITE) #Clears the window for each iteration
        window.blit(ball.image, (ball.x, ball.y)) #Draws the ball in the window
        
        #Draws the rackets
        window.blit(racket1.image, (racket1.x, racket1.y)) 
        window.blit(racket2.image, (racket2.x, racket2.y)) 
        
        
        text = f"Player 1 -> {ball.score} VS {ball.bot_score} <- Player 2" #Variable for display the text
        scoreboard = letters.render(text, False, BLACK) #Draws the text and give it color
        window.blit(scoreboard, ((WINDOW_W / 2) - (letters.size(text)[0] / 2), 50)) #Determines the position of the text
        
        for event in pygame.event.get():
            if event.type == QUIT: #In case that the window closes stops the loop
                playing = False
            
            #Checks if the key was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    racket1.dir_y = -10 #Moves the left racket up
                
                if event.key == pygame.K_s:
                    racket1.dir_y = 10 #Moves the left racket down
                
                if event.key == pygame.K_UP: #Moves the right racket up
                    racket2.dir_y = -10
                    
                if event.key == pygame.K_DOWN: #Moves the right racket down
                    racket2.dir_y = 10
            
            #Checks if the key was released
            if event.type == pygame.KEYUP:
                #Stops the rackets
                if event.key == pygame.K_w:
                    racket1.dir_y = 0 
                
                if event.key == pygame.K_s:
                    racket1.dir_y = 0 
                    
                if event.key == pygame.K_UP:
                    racket2.dir_y = 0
                    
                if event.key == pygame.K_DOWN:
                    racket2.dir_y = 0
                    
                    
        pygame.display.flip() #Redraws all of the elements in the window
        pygame.time.Clock().tick(FPS) #Mantain in check the speed of execution at the FPS value
        
    pygame.quit() #Stops all the process in case of quiting the game
    return True
    
#if __name__ == "__main__": #Executes the main function
#    main()