import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
fps = 45
b=1
counter = 0
background_image = pygame.image.load("bg.png")
def counter_round():
	global b,fps
	b +=1
	fps +=3  
def play_background_music():
    pygame.mixer.music.load("fon4.WAV")
    pygame.mixer.music.play(-1)  

class Sound():
	def __init__(self,sound):
		self.sound = sound  

	def pulya_sound(self):
		 	self.sound = pygame.mixer.Sound("pulya.mp3")
		 	self.sound.set_volume(1)
		 	self.sound.play()
	def destroyed_ball(self):
		self.sound = pygame.mixer.Sound("puzir.mp3")
		self.sound.set_volume(1)
		self.sound.play()
	def new_raund_sound(self):
		self.sound = pygame.mixer.Sound("smena1.mp3")
		self.sound.set_volume(1)
		self.sound.play()
	def game_over(self):
		self.sound = pygame.mixer.Sound("gover.mp3")
		self.sound.set_volume(1)
		self.sound.play()

class Write():
	def __init__(self,color = None,font =(None,32),text = None):
		self.text = text
		self.color = color or ((25,100,255))
		self.font = font

	def round(self):
		font = pygame.font.Font(self.font[0],self.font[1])
		text = font.render('RAUND:' + str(b),True,self.color)
		textRect = text.get_rect()
		textRect.center = (85,50)
		screen.blit(text,textRect)

	def destroyed_balls(self):
		font = pygame.font.Font(self.font[0],self.font[1])
		text = font.render('KILLED:' + str(counter),True,self.color)
		textRect = text.get_rect()
		textRect.center = (85,70)
		screen.blit(text,textRect)

	def totall_balls(self):
		global a
		font = pygame.font.Font(self.font[0],self.font[1])
		text = font.render('BALLS:' + str(len(balls)),True,self.color)
		textRect = text.get_rect()
		textRect.center = (87,90)
		screen.blit(text,textRect)

	def paused(self):
		 font = pygame.font.Font(self.font[0],self.font[1] )
		 text = font.render("You Lose !", True, 'red')
		 textRect = text.get_rect()
		 textRect.center = (400,300)
		 screen.blit(text,textRect)

	def retry(self):
		font = pygame.font.Font(self.font[0],self.font[1] )
		text = font.render('Retry: Press /Y   Exit : /N' , True, 'green')
		textRect = text.get_rect()
		textRect.center = (400,330)
		screen.blit(text,textRect)

class puwka():
	def __init__(self,x,y,color= None,left = False,right = False):
		self.left = left
		self.right = right
		self.x = x
		self.y = y 
		if color == None:
			color = ((255,0,0)) 
		self.color = color
		self.image = pygame.image.load("cannon.png")
		self.speed = 8

	def border_control(self):
		if self.x < 0:
			self.x= 0
		elif self.x + self.image.get_width() > 800:
			self.x = 805 - self.image.get_width()

	def control(self):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.x -=  self.speed
			if event.key == pygame.K_RIGHT:
				self.x  += self.speed 
				

	def update(self):
		global paused
		self.rect = pygame.Rect(self.x,self.y+50,60,50)
		for ball in balls:
			if self.rect.colliderect(ball.rect):
				sound_object.game_over()
				paused = True

class Pulya(puwka):
	def __init__(self,x,y,color = None,Shoot= False):
		super().__init__(x,y,color,Shoot)

		self.x = x 
		self.y = y 
		self.Shoot = Shoot
		if color == None:
			color = ((0,0,0))
		self.color = color
		self.speed = 8
		self.mvspeed = 23
		self.image = pygame.image.load("pulya.png")

		
	def vistrel(self):
		if self.Shoot:
			self.y -= self.mvspeed
		if self.y < 0:
			self.y = 630
			self.Shoot = False

	def pulya_border_control(self):
		if self.x < 35:
			self.x = 35
		if self.x >758:
			self.x = 758

	def update(self):
		global counter
		self.rect = pygame.Rect(self.x,self.y+33,20,33)
		for ball in balls:
			if self.rect.colliderect(ball.rect):
				sound_object.destroyed_ball()
				print('tegdi')
				balls.remove(ball)
				counter +=1
			
		
	def	shoot_bullet(self):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				self.Shoot = True
				sound_object.pulya_sound()		
			   
class Ball():
	def __init__(self,x,y,color= None,rad=27):
		self.rad = rad
		if color == None:
			color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.color = color
		self.image = pygame.Surface((self.rad * 2, self.rad * 2), pygame.SRCALPHA)
		pygame.draw.circle(self.image, self.color, (self.rad, self.rad), self.rad)
		self.vx = random.randint(-5, 5)
		self.vy = random.randint(1,   2)
		self.x = x if x and y else random.randint(self.rad, 800 - self.rad)
		self.y = y if x and y else random.randint (self.rad,300 - self.rad)
		self.rect = pygame.Rect(self.x,self.y,self.rad*2,self.rad*2)

	def update(self):
		self.rect = pygame.Rect(self.x,self.y,self.rad*2,self.rad*2)     
		friction = 1 
		self.vy *= friction
		self.y += self.vy
		if self.y == 0:
		 	self.y = 0
		 	self.vy = -self.vy
		elif self.y + self.rad * 2 > 630:
		 	self.x = random.randint(self.rad, 780 - self.rad*2)
		 	self.y = 600 - self.rad * 2
		 	self.y = self.rad /100
		 	self.vy = +self.vy

sound_object = Sound(None)
write_object = Write()
pulya_object = Pulya(400 ,660)
puwka_object = puwka(365,510)
a = 8
balls = [Ball(None,None) for i in range(a)]
def new_raund():
	global a
	a +=1
	for ball in range(a):
	  balls.append(Ball(None,None))
paused = False
play_background_music()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False 
    elif event.type == pygame.KEYDOWN:
    	if paused:
    		 if event.key == pygame.K_y:
     				paused = False
     				fps =45
    		 elif event.key == pygame.K_n:
    				running = False 
    pulya_object.shoot_bullet()
  	
  pulya_object.update()
  puwka_object.control()
  pulya_object.control()
  pulya_object.vistrel()
  puwka_object.border_control()
  pulya_object.pulya_border_control()
  for ball in balls:
  	ball.update()


  screen.blit(background_image,(0,0))
   
  if puwka_object.update():

	     		paused = True
  
  for ball in balls:
    ball.update()
    screen.blit(ball.image,(ball.x,ball.y)) 

  screen.blit(pulya_object.image,(pulya_object.x,pulya_object.y))
  screen.blit(puwka_object.image,(puwka_object.x,puwka_object.y))

  write_object.destroyed_balls() 
  write_object.round()
  write_object.totall_balls()
  if paused:
  	write_object.paused()
  	write_object.retry()
  	fps=5
   
  if len(balls) == 0:
  	counter_round()  
  	new_raund() 
  	sound_object.new_raund_sound()

  pygame.display.flip()

  clock.tick(fps)

pygame.quit()
