#!/usr/bin/env python3

import pygame
import time
import random

pygame.init()

FPS = 60

display_width = 800
display_height = 600

#color definition
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)

gameDisplay = pygame.display.set_mode( (display_width,display_height) )#setup window for game with dimensions as tuple
pygame.display.set_caption('CyberSpace') #changes window title
clock = pygame.time.Clock()#game time / FPS controller

rocketImg = pygame.image.load('assets/badass-rocket.png').convert()
rocketImg2 = pygame.image.load('assets/badass-rocket2.png').convert()
rocketImg3 = pygame.image.load('assets/badass-rocket3.png').convert()

FloppyImg = pygame.image.load('assets/floppy.png').convert()
EmailImg = pygame.image.load('assets/email.png').convert()

#Peformance Increase on older machines with '.convert()' function

Background = pygame.image.load('assets/cyberspace2.png') #not to  be used until easier to see
CyberFont = pygame.font.Font('assets/computer_pixel-7.ttf',30)

rocket_width = 30
rocket_height = 66

def things_dodged(count ,speed, font, colour):
	text = font.render("Dodged: "+str(count), True, colour)
	text2 = font.render("Speed: "+str(speed)+' / '+str(FPS)+"FPS", True, colour)
	gameDisplay.blit(text,(0,0))
	gameDisplay.blit(text2,(0,30))

def things(thingx, thingy, thingw, thingh, thing_Type):
    #the coordinates for the obstacles to draw
	gameDisplay.blit(thing_Type,(thingx,thingy, thingw, thingh)) #boundaries are applicable to collision

def rocket(x,y,listOfRockets): #function to draw awesome graphic
	thruster_adjust = random.choice(listOfRockets) #small utility for thruster animation (chooses from rocket images)
	gameDisplay.blit(thruster_adjust,(x,y)) #blit draws on gameDisplay at specified coordinates

def background():
	gameDisplay.blit(Background,(0,0))

def message_display(text, font):
	TextSurf, TextRect = text_objects(text, font, GREEN)
	TextRect.center = (display_width / 2, display_height / 2-40)
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()

def text_objects(text, font, colour):
	textSurface = font.render(text, True, colour)
	return textSurface, textSurface.get_rect()

def kerploo(message): #when enemy is destroyed
	message_display(message, CyberFont)

def collide(ax, ay, aw, ah, bx, by, bw, bh):
	return ax < bx+bw and ay < by+bh and bx < ax+aw and by < ay+ah

def thing_return(listOfThings):
	thing_type = random.choice(listOfThings)
	if thing_type == FloppyImg:
		width = 100
	else:
		width = 150
	return [thing_type, width]

def game_loop():
	
	list_rockets = [rocketImg, rocketImg2, rocketImg3]
	x_rocket = (display_width * 0.45) #rad rocket coordinates
	y_rocket = (display_height * 0.8)

	x_change = 0

	thing_list = [FloppyImg,EmailImg]
	thing_startx = random.randrange(0, (display_width - 100))
	thing_starty = -600
	thing_speed = 3 
	floppy_width = 100
	thing_height = 100
	email_width = 150
	thing_type = thing_return(thing_list)

	dodged = 0
	gameExit = False #condition for the game to keep running

	while not gameExit:

		for event in pygame.event.get(): #pygame.event.get() gets user input for event handling
			if event.type == pygame.QUIT: # if the player hits the X button
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN: # if the player presses a key...
				if event.key == pygame.K_LEFT: # if the key pressed was left...
					x_change = -7 #change x by -5
				elif event.key == pygame.K_RIGHT:
					x_change = 7

			if event.type == pygame.KEYUP: # condition if the key pressed was lifted
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # condition if keys were left or right
					x_change = 0 # stop moving

            #print(event) #tells you what events are occuring

		x_rocket += x_change # apply x axis changes for crisp animation

		#background()#creates new frame by drawing over last frame
		gameDisplay.fill(BLACK)
		things(thing_startx, thing_starty, thing_type[1], thing_height,thing_type[0])
		thing_starty += thing_speed
		rocket(x_rocket, y_rocket, list_rockets ) #function call to display badass-rocket
		things_dodged(dodged, thing_speed, CyberFont, GREEN)

		if x_rocket > display_width - rocket_width or x_rocket < 0: #if rocket goes beyond epic walls, stop movement exploitable bug that needs to be fixed
			x_change = 0

        #resets obstacle(s)
		if thing_starty > display_height:
			thing_type = thing_return(thing_list)
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,(display_width - (thing_type[1] - 1))) # -1 included to avoid sprite duplication along borders
			dodged += 1
			thing_speed += 0.25

		if collide(x_rocket,y_rocket,rocket_width,rocket_height,thing_startx,thing_starty,thing_type[1],thing_height):
			kerploo("GAME OVER")
	   
		pygame.display.update() #updates the window completely
		clock.tick(FPS) #frames per second control




game_loop()
pygame.quit()
quit()
