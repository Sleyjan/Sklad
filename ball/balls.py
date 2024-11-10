import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))


clock = pygame.time.Clock()
fps = 60

class Ball():
	def __init__(self,x,y,color= None,rad=30):

		self.rad = rad

		if color == None:
			color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

		self.color = color

		self.image = pygame.Surface((self.rad * 2, self.rad * 2), pygame.SRCALPHA)

		pygame.draw.circle(self.image, self.color, (self.rad, self.rad), self.rad)
		

		self.vx = random.randint(-5, 5)

		self.vy = random.randint(1, 2)

		self.x = x if x and y else random.randint(self.rad, 800 - self.rad)

		self.y = y if x and y else random.randint(self.rad, 600 - self.rad)

	def update(self):
        
		 friction = 1  # Adjust for desired friction level (0 to 1)
		 self.vx *= friction 
		 self.vy *= friction
		 #self.x += self.vx
		 self.y += self.vy

        
		 #if self.x < 0:
		 #	self.x = 0
		 	#self.vx = -self.vx
		 #elif self.x + self.rad * 2 > 800:
		 	#self.x = 800 - self.rad * 2
		 #	self.vx = -self.vx

		 if self.y == 0:
		 	self.y = 0
		 	self.vy = -self.vy
		 elif self.y + self.rad * 2 > 600:

		 	self.x = random.randint(self.rad, 800 - self.rad)
		 	self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		 	self.y = 600 - self.rad * 2
		 	self.y = self.rad /100
		 	self.vy = +self.vy

balls = [Ball(None,None) for i in range(6)]
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
 	
  screen.fill((0,0,0))

  for ball in balls:
    ball.update()
    screen.blit(ball.image,(ball.x,ball.y))

  pygame.display.flip()

  clock.tick(fps)

pygame.quit()
