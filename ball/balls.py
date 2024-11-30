import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
fps = 45
b=1
colidion = False
health = 0
counter = 0
bombed = 0
background_image = pygame.image.load("bg1.png")
fly = False
bomb = False

class Heart():
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.image = pygame.image.load("heart1.png")

	def photo_heart(self):
		screen.blit(self.image,(self.x,self.y))
def fly_control():
	global fly,bomb
	if fly == True:
		sound_object.fly_sound()
		fly1.move_fly()
		bomb = True
		if fly1.x >=820:
			fly1.x = -200
			fly = False
def bomb_control():
	global bomb
	if bomb == True:
		bomb1.move()

		if bomb1.y + bomb1.image.get_width() >=950:
			sound_object.boom()
			bomb1.y = 0
			bomb1.x = 0
			bomb = False			

def counter_round():
	global b,fps
	if stop ==True:
		b +=1
		fps +=3  
def play_background_music():
    pygame.mixer.music.load("fonnmusik1.WAV")
    pygame.mixer.music.play(-1)  

class Sound():
	def __init__(self,sound):
		self.sound = sound  
	def boom(self):
			self.sound = pygame.mixer.Sound("boom.WAV")
			self.sound.set_volume(1)
			self.sound.play()

	def fly_sound(self):
		 	self.sound = pygame.mixer.Sound("fly.WAV")
		 	self.sound.set_volume(1)
		 	self.sound.play()
	def pulya_sound(self):
		 	self.sound = pygame.mixer.Sound("pulya1.WAV")
		 	self.sound.set_volume(1)
		 	self.sound.play()
	def destroyed_ball(self):
		self.sound = pygame.mixer.Sound("puzir.mp3")
		self.sound.set_volume(1)
		self.sound.play()
	def new_raund_sound(self):
		self.sound = pygame.mixer.Sound("smena.WAV")
		self.sound.set_volume(1)
		self.sound.play()
	def game_over(self):
		self.sound = pygame.mixer.Sound("gover.mp3")
		self.sound.set_volume(1)
		self.sound.play()

class Write():
	def __init__(self,color = None,font =(None,32),text = None):
		self.text = text
		self.color = color or ((255,255,255))
		self.font = font

	def round(self):
		font = pygame.font.Font(self.font[0],self.font[1])
		text = font.render('RAUND:' + str(b),True,self.color)
		textRect = text.get_rect()
		textRect.center = (85,50)
		screen.blit(text,textRect)

	def destroyed_balls(self):
		font = pygame.font.Font(self.font[0],self.font[1])
		text = font.render('SCORE:' + str(counter),True,self.color)
		textRect = text.get_rect()
		textRect.center = (85,80)
		screen.blit(text,textRect)

	def totall_balls(self):
		global a
		font = pygame.font.Font(self.font[0],self.font[1])
		text = font.render('BALLS:' + str(len(balls)),True,self.color)
		textRect = text.get_rect()
		textRect.center = (85,110)
		screen.blit(text,textRect)

	def health_puwka(self):
		 global health
		 font = pygame.font.Font(None,42 )
		 text = font.render(" = "+str(3-math.floor(bombed)), True, 'red')
		 textRect = text.get_rect()
		 textRect.center = (666,73)
		 screen.blit(text,textRect)

	def Game_over(self):
		font = pygame.font.Font(None,72 )
		text = font.render('GAME OVER :/' , True, 'red')
		textRect = text.get_rect()
		textRect.center = (400,280)
		screen.blit(text,textRect)

class FLYER():
	def __init__(self,x,y,speed):
		self.image = pygame.image.load("fly.png")
		self.x = x 
		self.y = y
		self.speed = speed
		self.rect = pygame.Rect(self.x,self.y,150,150)
	def move_fly(self): 
		self.x += self.speed		

	def return_back(self):
			self.x = -200

class Bomb(FLYER):
	def __init__(self,x,y,speed = 10):
		super().__init__(x,y,speed)

		self.x = x
		x = fly1.x
		self.y = y
		y = fly1.y
		self.speed = speed  
		self.image=pygame.image.load("bomb1.png")
		self.rect = pygame.Rect(self.x,self.y,80,80) 
		self.image1 = pygame.image.load("boom.png")

	def draw(self):
		screen.blit(self.image,(self.x,self.y))
	def draw1(self):
		screen.blit(self.image1,(self.x,self.y))

	def move(self):
		if puwka_object.rect.x <400:
			self.x += self.speed*0.5
			self.y += self.speed*1.2
		else:
			self.x += self.speed
			self.y += self.speed*0.8


	def update(self):
		global stop,bombed
		self.rect = pygame.Rect(self.x,self.y,50,50)
		if self.rect.colliderect(puwka_object.rect):
			bombed += 1*0.1
			if bombed >= 3:
				stop = False
				balls.clear()


class puwka():
	def __init__(self,x,y,color= None,left = False,right = False):
		
		self.x = x
		self.y = y 
		if color == None:
			color = ((255,0,0)) 
		self.color = color
		self.image = pygame.image.load("cannon.png")
		self.rect = pygame.Rect(self.x,self.y+50,60,50)
		self.speed = 8

	def border_control(self):
		if self.x < 0:
			self.x= 0
		elif self.x + self.image.get_width() > 800:
			self.x = 800 - self.image.get_width()

	def control_left(self):
			self.x -=  self.speed

	def control_right(self):
				self.x  += self.speed 	
		
	def update(self):

		global health,colidion,fly,bomb
		self.rect = pygame.Rect(self.x,self.y+50,60,50)
		for ball in balls:
			if self.rect.colliderect(ball.rect):
				fly = True
				sound_object.game_over()
				colidion= True
				fps =1
				#bomb = True
			else:
				colidion = False

class Pulya():
	def __init__(self,x,y,color = None,Shoot= False,speed =8):
		self.x = x 
		self.y = y 
		self.speed = speed
		self.Shoot = Shoot
		if color == None:
			color = ((0,0,0))
		self.color = color
		self.mvspeed = 35
		self.image = pygame.image.load("pulya4.png")
		self.rect = pygame.Rect(self.x,self.y+33,20,33)
		
	def vistrel(self):
		if self.Shoot:
			self.y -= self.mvspeed
		if self.y < 0:
			self.y = 630
			self.Shoot = False
	def control_left(self):
			self.x -=  self.speed

	def control_right(self):
				self.x  += self.speed

	def pulya_border_control(self):
		if self.x < 25:
			self.x = 25
		if self.x >745:
			self.x = 745

	def update(self):
		global counter
		self.rect = pygame.Rect(self.x,self.y+33,20,33)
		for ball in balls:
			if self.rect.colliderect(ball.rect):
				sound_object.destroyed_ball()

				balls.remove(ball)
				if stop == True:
					counter +=1
	def	shoot_bullet(self):
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
		self.x = x if x and y else random.randint(self.rad, 775 - self.rad)
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

class draw():
	def __init__(self):
		pass

	def draw_objects(self):
		global health,colidion
		screen.blit(background_image,(0,0))
		for ball in balls:
		  ball.update()
		  screen.blit(ball.image,(ball.x,ball.y))
		screen.blit(pulya_object.image,(pulya_object.x,pulya_object.y))
		screen.blit(puwka_object.image,(puwka_object.x,puwka_object.y))
		screen.blit(fly1.image,(fly1.x,fly1.y))
		Heart1.photo_heart()

		write_object.destroyed_balls()
		write_object.round()
		write_object.totall_balls()
		write_object.health_puwka()

		if bombed >=3:
			write_object.Game_over()
		if fly1.x >= puwka_object.rect.x:
			bomb1.draw()

		if bomb1.rect.y >=400 and bomb1.rect.y <=550:
				bomb1.draw1()

class MainLoop():
	def __init__(self,x,y,color=None,event=None):
		self.x = x
		self.y = y

	def menenger(self):
		global fps,health,stop,bombed,bomb
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						pulya_object.shoot_bullet()
				
			if event.type == pygame.KEYDOWN:			
					if event.key == pygame.K_LEFT:
						puwka_object.control_left()
						pulya_object.control_left()

					if event.key == pygame.K_RIGHT:
						puwka_object.control_right()
						pulya_object.control_right()

			
			for ball in balls:
					ball.update()
					pulya_object.update()
					puwka_object.update()
			bomb1.update()
			pulya_object.vistrel()
			puwka_object.border_control()
			pulya_object.pulya_border_control()
			if bombed >=3:
				stop = False
				balls.clear()
			fly_control()
			bomb_control()

			if len(balls) == 0 and stop == True:
				counter_round()
				new_raund()
				sound_object.new_raund_sound()	
			draw1.draw_objects()		
			pygame.display.flip()
			clock.tick(fps)

Heart1 = Heart(600,50)
fly1 = FLYER(-200,100,20)
draw1 = draw()
sound_object = Sound(None)
write_object = Write()
pulya_object = Pulya(385 ,660)
puwka_object = puwka(365,510)
bomb1 = Bomb(0,0,12)
MainLoop1 =MainLoop(None,None)
stop = True
a = 8
balls = [Ball(None,None) for i in range(a)]
def new_raund():
	global a,stop
	if stop == True:
		a +=1
		for ball in range(a):
			balls.append(Ball(None,None))

play_background_music()

MainLoop1.menenger()
pygame.quit()