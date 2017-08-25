#!/usr/bin/env python3

import pygame
import time
import random

pygame.init()

FPS = 30

display_width = 800
display_height = 600

#color definition
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)

clock = pygame.time.Clock()#game time / FPS controller
gameDisplay = pygame.display.set_mode( (display_width,display_height) )#setup window for game with dimensions as tuple
pygame.display.set_caption('CyberSpace is running at '+str(int(clock.get_fps()))+' FPS') #changes window title

rocketImg = pygame.image.load('assets/badass-rocket.png').convert()
rocketImg2 = pygame.image.load('assets/badass-rocket2.png').convert()
rocketImg3 = pygame.image.load('assets/badass-rocket3.png').convert()

FloppyImg = pygame.image.load('assets/floppy.png').convert()
EmailImg = pygame.image.load('assets/email.png').convert()

Background = pygame.image.load('assets/cyberspace2.png') #not to  be used until easier to see
CyberFont = 'assets/computer_pixel-7.ttf'

#All sound from freesound.org
pygame.mixer.music.load("assets/in_gamemusic.mp3")
point_get = pygame.mixer.Sound('assets/point.wav')
select = pygame.mixer.Sound('assets/select.wav')
game_start = pygame.mixer.Sound('assets/explosion1.wav')
kerploo_sound = pygame.mixer.Sound('assets/kerploo.wav')

rocket_width = 30
rocket_height = 66

def thing1(thingx, thingy, thingw, thingh, thing_Type): #low-key Dr Seuss reference ;)
    #the coordinates for the obstacles to draw
	gameDisplay.blit(thing_Type,(thingx,thingy, thingw, thingh)) #boundaries are applicable to collision

def thing2(thingx, thingy, thingw, thingh, thing_Type):
	gameDisplay.blit(thing_Type,(thingx,thingy, thingw, thingh))

def rocket(x,y,listOfRockets): #function to draw awesome graphic
	thruster_adjust = random.choice(listOfRockets) #small utility for thruster animation (chooses from rocket images)
	gameDisplay.blit(thruster_adjust,(x,y)) #blit draws on gameDisplay at specified coordinates

def background():
	gameDisplay.blit(Background,(0,0))

def collide(ax, ay, aw, ah, bx, by, bw, bh):
	return ax < bx+bw and ay < by+bh and bx < ax+aw and by < ay+ah

def thing_return(listOfThings):
	thing_type = random.choice(listOfThings)
	if thing_type == FloppyImg:
		width = 100
	else:
		width = 150
	return [thing_type, width]

def message_render(message, font, size, colour): #replace any things that use render with this function to avoid repetition
	text_font = pygame.font.Font(font, size)
	text_message = text_font.render(message,True ,colour )
	
	return text_message

def game_intro():
	
	intro = True

	menuChoice = 'play'

	title = message_render("CyberSpace", CyberFont, 115, GREEN)

	while intro:
		pygame.display.set_caption('CyberSpace is running at '+str(int(clock.get_fps()))+' FPS') #changes window title
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					pygame.mixer.Sound.play(select)
					menuChoice = 'play'
					pygame.mixer.Sound.play(select)
				elif event.key == pygame.K_DOWN:
					pygame.mixer.Sound.play(select)
					menuChoice = 'quit'
				elif event.key == pygame.K_RETURN:
					if menuChoice == 'play':
						pygame.mixer.Sound.play(game_start)
						time.sleep(1)
						game_loop()
					elif menuChoice == 'quit':
						#returns error and crashes but it does its intended purpose (fix if desired but isn't needed)
						pygame.quit()
						quit()
			print(event)

		if menuChoice == 'play':
			start = message_render("Start",CyberFont, 75, GREEN)
		else:
			start = message_render("Start",CyberFont, 75, WHITE)
		if menuChoice == 'quit':
			quit = message_render("Quit",CyberFont, 75, GREEN)
		else:
			quit = message_render("Quit",CyberFont, 75, WHITE)


		gameDisplay.fill(BLACK)
		#using the center of screen as a base and adjusting distances to liking
		watermark = message_render("github/HeartDruid1",CyberFont, 30, GREEN)
		gameDisplay.blit(watermark,(0,570))
		gameDisplay.blit(title,(200, 100))
		gameDisplay.blit(start,(display_width / 2 - 100, display_height / 2))
		gameDisplay.blit(quit,(display_width / 2 - 100 , display_height / 2 + 40))
		
		pygame.display.update()
		clock.tick(FPS)

def kerploo():
	kerploo = message_render("GAME OVER!",CyberFont,30,GREEN)
	gameDisplay.blit(kerploo,((display_width / 2)-30, display_height / 2))
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(kerploo_sound)
	pygame.display.update()

def game_loop():
	pygame.mixer.music.play(-1)
	pygame.display.set_caption('CyberSpace is running at '+str(int(clock.get_fps()))+' FPS') #changes window title

	list_rockets = [rocketImg, rocketImg2, rocketImg3]
	x_rocket = (display_width * 0.45) #rad rocket coordinates
	y_rocket = (display_height * 0.8)

	x_change = 0

	thing_list = [FloppyImg,EmailImg]
	thing1_startx = random.randrange(0, (display_width - 100))
	thing2_startx = random.randrange(0, (display_width - 100))
	thing1_starty = random.randrange(-600, 0)
	thing2_starty = random.randrange(-600, 0)
	thing_speed = 5 
	floppy_width = 100
	thing_height = 100
	email_width = 150
	thing1_type = thing_return(thing_list)
	thing2_type = thing_return(thing_list)

	dodged = 0
	gameExit = False #condition for the game to keep running

	while not gameExit:

		for event in pygame.event.get(): #pygame.event.get() gets user input for event handling
			if event.type == pygame.QUIT: # if the player hits the X button
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN: # if the player presses a key...
				if event.key == pygame.K_LEFT: # if the key pressed was left...
					x_change = -7 #change x by -7
				elif event.key == pygame.K_RIGHT:
					x_change = 7

			if event.type == pygame.KEYUP: # condition if the key pressed was lifted
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # condition if keys were left or right
					x_change = 0 # stop moving
			print(event) #debug tool 

		x_rocket += x_change

		#background()#creates new frame by drawing over last frame
		gameDisplay.fill(BLACK)
		thing1(thing1_startx, thing1_starty, thing1_type[1], thing_height, thing1_type[0])
		thing2(thing2_startx, thing2_starty, thing2_type[1], thing_height, thing2_type[0])
		thing1_starty += thing_speed
		thing2_starty += thing_speed
		rocket(x_rocket, y_rocket, list_rockets) #function call to display badass-rocket

		#display text
		dodged_text = message_render("Data Clusters Passed: "+str(dodged), CyberFont, 30,GREEN)
		speed_text = message_render("Download Speed: "+str(thing_speed)+"Kb/s",CyberFont,30,GREEN)
		gameDisplay.blit(dodged_text,(0,0))
		gameDisplay.blit(speed_text,(0,30))
		

		if x_rocket > display_width - rocket_width: #if rocket goes beyond epic walls stop movement and set X value to the border
			print('right wall')
			x_change = 0
			x_rocket = display_width - rocket_width

		elif x_rocket < 0:
			print('left wall')
			x_change = 0
			x_rocket = 0

        #resets obstacle(s)
		if thing1_starty > display_height:
			thing1_type = thing_return(thing_list)
			thing1_starty = random.randrange(-400, 0)
			thing1_startx = random.randrange(0,(display_width - (thing1_type[1] - 1))) # -1 included to avoid sprite duplication along borders
			thing_speed += 0.25
			dodged += (random.randint(1,5) + thing_speed)
			pygame.mixer.Sound.play(point_get)

		if thing2_starty > display_height:
			thing2_type = thing_return(thing_list)
			thing2_starty = random.randrange(-400, 0)
			thing2_startx = random.randrange(0,(display_width - (thing2_type[1] - 1)))
			thing_speed += 0.25
			dodged += (random.randint(1,5) + thing_speed)
			pygame.mixer.Sound.play(point_get)

		if collide(x_rocket,y_rocket,rocket_width,rocket_height,thing1_startx,thing1_starty,thing1_type[1],thing_height):
			print("Collide")
			kerploo()
			time.sleep(2)
			game_loop()
	  
		if collide(x_rocket,y_rocket,rocket_width,rocket_height,thing2_startx,thing2_starty,thing2_type[1],thing_height):
			print("Collide")
			kerploo()
			time.sleep(2)
			game_loop()

 
		pygame.display.update() #updates the window completely
		clock.tick(FPS) #frames per second control



game_intro()
game_loop()
pygame.quit()
quit()
