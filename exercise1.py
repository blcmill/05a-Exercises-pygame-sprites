#!/usr/bin/env python
'''

For every line, please add a comment describing what it does.

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first few lines for you as an example


'''
import sys, logging, pygame	# imports the sys, logging, and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

logging.basicConfig(level=logging.CRITICAL) #Sets up the logger as a critical level logger
logger = logging.getLogger(__name__) # Instantiates a logger for the file using "__name__"

screen_size = (800,600) #Sets the screen size to a tuple, assumedly x by y
FPS = 60 #assigns an integer to "FPS", supposedly the number of times per second a frame should be rendered
red = (255,0,0) #assigns a tuple to "red", with the RGB code of red, to be used to render color
black = (0,0,0) #assigns a tuple to "black", with the RGB code of black, to be used to render color

class Block(pygame.sprite.Sprite): #Defines the block class, which will be rendered
	def __init__(self, position, direction): #This function initializes a block using three variables
		pygame.sprite.Sprite.__init__(self) #This function initializes the block as a sprite
		self.image = pygame.Surface((50, 50)) # Makes the image a flat surface of dimensions 50x50
		self.image.fill(red) #Fills the image with the color assigned to the tuple "red"
		self.rect = self.image.get_rect() #gets the pygame position of the rectangle
		(self.rect.x,self.rect.y) = position #sets position of self to be the position of the rect
		self.direction = direction #direction is saved here

	def update(self): #This function is called every update (60 times/second)
		(dx,dy) = self.direction # Change in direction x and y should be equal to direction
		self.rect.x += dx #Adds to the x position the dx
		self.rect.y += dy #Adds to the y position the dy
		(WIDTH,HEIGHT) = screen_size # assigns WIDTH to be the x of screen size and HEIGHT to be the y of screen size
		if self.rect.left > WIDTH: #If the left part of the rectangle passes the right side:
			self.rect.right = 0 #the right part of the rectangle goes to the left side (with the whole thing)
		if self.rect.right < 0: #If the right side of the rectangle passes the left side:
			self.rect.left = WIDTH #the left part of the rectangle goes to the left side (with the whole thing)
		if self.rect.top > HEIGHT: #If the top of the rectangle exceeds the top:
			self.rect.bottom = 0 #Bottom of the rectangle pos is the bottom now
		if self.rect.bottom < 0: #If the bottom of the rectangle goes below zero:
			self.rect.top = HEIGHT #Rectangle teleports to the top!


def main(): #Main function
	pygame.init() #Initializes pygame
	screen = pygame.display.set_mode(screen_size) #Initializes screen using variable
	clock = pygame.time.Clock() #Initializes pygame clock

	blocks = pygame.sprite.Group() #Creates new group called blocks
	block = Block((200,200),(-1,1)) #instantiates a block with position 200,200, and direction -1, 1, so it will go down-left
	blocks.add(block) #adds block to the blocks group

	while True: #main game loop
		clock.tick(FPS) #wait 1/60 of a second
		screen.fill(black) #fill screen with black

		for event in pygame.event.get(): #Event handler
			if event.type == pygame.QUIT: #if someone quits:
				pygame.quit() #quit pygame
				sys.exit(0) #exit python

		blocks.update() #update blocks
		blocks.draw(screen) #draw blocks
		pygame.display.flip() #flip the display to render properly

if __name__ == '__main__': #if this is run as a module:
	main() #run main
