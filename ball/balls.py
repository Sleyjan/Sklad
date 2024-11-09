import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))


clock = pygame.time.Clock()
clock.tick(15)

class Ball():
	def __init__(self,coord= None,color= None,rad=30):

		if coord == None:
			coord =(random.randint(0,800-rad),random.randint(0,600-rad))
		self.coord =list(coord)
		if color == None:
			color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.color = color
		self.rad = rad	
		self.vx =	random.randint(-10,10)
		self.vy = random.randint(-10,10)

	def update(self):
        self.image = pygame.draw.circle(screen, self.color, self.coord, self.rad)
        self.coord[0] += self.vx
        self.coord[1] += self.vy

		if self.coord[0]<0 or self.coord[0] + self.rad*2>800:
			self.vx = -self.vx
		if self.coord[1] < 0 or self.coord[1] + self.rad*2 >600:
			self.vy = -self.vy
balls=[]
for i in range(10):
	ball = Ball()
	balls.append(ball)


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      runing = False
  # Correct indentation (assuming 2 spaces)
  for ball in balls:
    ball.update()
    screen.blit(ball.image, ball.coord)
  pygame.display.flip()
