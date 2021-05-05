import pygame
import math
import sys


pygame.init()

FPS = 60

screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()

BLACK = (0,0,0) 

class camera:
	x = 0
	y = 0 

class object:
	x = 0
	y = 0
	image = None #NONE for install to this image use setObj(self, image)
	@staticmethod #all methods are avaible
	def setObj(self, image):
		#IMAGE = pygame.Surface {image}
	@staticmethod
	def new(self, coord):
		#COORD = list({x,y})
		if self.image != None:
			self.x = coord[0]
			self.y = coord[1]
		else:
			print("Dont use setObj() func in " + str(self))
	@staticmethod
	def update(self, screen):
		screen.blit(self.image, (self.x-camera.x,self.y-camera.y))
x = 0
y = 0
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		y -= 3
	if keys[pygame.K_a]:
		x -= 3
	if keys[pygame.K_s]:
		y += 3
	if keys[pygame.K_d]:
		x += 3
	# Vector from me to cursor
	cursor_pos = pygame.mouse.get_pos()	
	cursor_x = cursor_pos[0]
	cursor_y = cursor_pos[1]
	
	speed = 3
	
	dx = cursor_x - x
	dy = cursor_y - y

	# Unit vector in the same direction
	distance = math.sqrt(dx*dx + dy*dy)
	dx /= distance
	dy /= distance

	# speed-pixel vector in the same direction
	dx *= speed
	dy *= speed

	# And now we move:
	x += dx
	y += dy	
	
	player = pygame.image.load("img/player.png")	
	screen.fill(BLACK)
	screen.blit(player, (x, y))
	pygame.display.update()
	clock.tick(FPS)
	
pygame.quit()
