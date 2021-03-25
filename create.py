import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


car_width = 50
car_height = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Car Raceing')
clock = pygame.time.Clock()

carImg = pygame.image.load('car2.png')
carImg2 = pygame.image.load('car1.png')
crashimg = pygame.image.load('crash.png') 

over_font = pygame.font.Font("freesansbold.ttf",45)

def line(lineX,lineY,lineW,lineH,color):
    pygame.draw.rect(gameDisplay,color,[lineX,lineY,lineW,lineH])

def highscore(count):
	font = pygame.font.SysFont(None,30)
	text = font.render("Score : "+str(count),True,black)
	gameDisplay.blit(text,(0,10))

def game_over_text(count):
    over_text = over_font.render("score :"+str(count),True,black)
    gameDisplay.blit(over_text,(0,0))

def text_objects(text,font):
	textSurface = font.render(text,True,red)
	return textSurface,textSurface.get_rect()

def message_display(text,size,x,y):
    font = pygame.font.Font("freesansbold.ttf",size)
    text_surface , text_rectangle = text_objects(text,font)
    text_rectangle.center =(x,y)
    gameDisplay.blit(text_surface,text_rectangle)
    

def crash(x,y):
    gameDisplay.blit(crashimg,(x,y))
    message_display("You Crashed",64,display_width/2,display_height/2)
    #message_display("GAME OVER",64,display_width/2,display_height/2)
    
    pygame.display.update()
    time.sleep(2)
    game_loop()


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def thing(x,y):
    gameDisplay.blit(carImg2,(x,y))

def game_loop():
    x = (display_width * 0.45) #360
    y = (display_height * 0.8) #480

    x_change = 0

    thing_startx = random.randrange(200,585 ) #0,display_width
    thing_starty = -600
    thing_speed = 8
    thing_width = 50 #y+
    thing_height = 100  #x+
    count = 0
    lineY = 0
    lineX = 400
    lineW = 20
    lineH = 450
    line_speed = 10
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                if event.key == pygame.K_RIGHT:
                    x_change = 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(white)
        line(150,0,20,display_height,black)
        line(display_width-170,0,20,display_height,black)
        thing(thing_startx,thing_starty)
        car(x,y)
        if x > display_width - car_width or x < 0: #800-73
            crash(x,y)
        if thing_starty > display_height: #-600 > 600
            thing_starty = 0 - thing_height #-600 = 0-100
            thing_startx = random.randrange(200,585)
        if y < thing_starty+thing_height: #-600+100
            if x > thing_startx and x < thing_startx + thing_width: 
                #print('x crossover')
                crash(x-25,y-car_height/2)
            if x +car_width > thing_startx and x + car_width < thing_startx+thing_width:
                crash(x,y-car_height/2)
        highscore(count)
        count += 1
        thing_starty += thing_speed


        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()