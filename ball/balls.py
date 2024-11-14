import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))


clock = pygame.time.Clock()
fps = 60

class puwka():
	def __init__(self,x,y,color= None,left = False,right = False):

		self.left = left
		self.right = right
		self.x = x
		self.y = y 
		if color == None:

			color = ((255,0,0))
		self.color = color

		self.image = pygame.Surface((100,600),pygame.SRCALPHA)

		pygame.draw.polygon(self.image, self.color, [[0 ,100], [35,50], [70,100]] )
		self.speed = 20


	def border_control(self):

		if self.x < 0:
			self.x= 0
		elif self.x + self.image.get_width() > 800:
			self.x = 820 - self.image.get_width()


	def control(self):

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.x -=  self.speed
			if event.key == pygame.K_RIGHT:
				self.x  += self.speed 

class Pulya(puwka):
	def __init__(self,x,y,color = None,rad=5,Shoot= False):
		super().__init__(x,y,color,Shoot)
		self.rad = rad
		self.x = x 
		self.y = y 
		self.Shoot = Shoot
		if color == None:
			color = ((255,5,5))
		self.color = color
		self.speed = 20
		self.mvspeed = 30
		self.image = pygame.Surface((self.rad*2,self.rad*2),pygame.SRCALPHA)
		pygame.draw.circle(self.image,self.color,(self.rad,self.rad),self.rad)
		
	def vistrel(self):

		if self.Shoot:
			self.y -= self.mvspeed

		if self.y < 0:
			self.y = 550
			self.Shoot = False


	def pulya_border_control(self):
		if self.x < 30:
			self.x = 30
		if self.x >750:
			self.x = 750



	def update(self):

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				self.Shoot = True
		self.rect = pygame.Rect(self.x,self.y,self.rad,self.rad)
		for ball in balls:
			if self.rect.colliderect(ball.rect):
				balls.remove(ball)

			   
class Ball():
	def __init__(self,x,y,color= None,rad=22):

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

		self.rect = pygame.Rect(self.x,self.y,self.rad*2,self.rad*2)

	def update(self):
        
		 friction = 1 
		 # self.vx *= friction 
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
		 	self.y = 600 - self.rad * 2
		 	self.y = self.rad /100
		 	self.vy = +self.vy
		 	
		 	self.rect = pygame.Rect(self.x,self.y,self.rad*2,self.rad*2)

pulya_object =Pulya(430,550)
puwka_object = puwka(400,495)

balls = [Ball(None,None) for i in range(8)]

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    puwka_object.control()
    pulya_object.control()
    pulya_object.update()
  for ball in balls:
   	ball.update()
  for ball in balls:
  	if pulya_object.rect.colliderect(ball.rect):

  		balls.remove(ball)

  pulya_object.vistrel()

  puwka_object.border_control()

  pulya_object.pulya_border_control()

  screen.fill((0,0,0))

  for ball in balls:
    ball.update()

    screen.blit(ball.image,(ball.x,ball.y))
  
  screen.blit(puwka_object.image,(puwka_object.x,puwka_object.y))
  screen.blit(pulya_object.image,(pulya_object.x,pulya_object.y))

  

  pygame.display.flip()

  clock.tick(fps)

pygame.quit()
