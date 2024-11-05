import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
all_sprites = pygame.sprite.Group()
class Ball(pygame.sprite.Sprite):
	def __init__(self,x,y):

		super().__init__()
		self.image = pygame.Surface((20,20))

		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		



for i in range(10):
	ball = Ball(i*30,50)
	all_sprites.add(ball)


clock = pygame.time.Clock()
clock.tick(60)
speed =random.randint(-5,5)

runing = True
while runing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runing = False

	for sprite in all_sprites:
		sprite.rect.y += speed
		sprite.rect.x +=speed
	if sprite.rect.x>=800:
		sprite.rect.x = 700
	elif sprite.rect.x <=0:
		sprite.rect.x = 100
	elif sprite.rect.y <=0:
		sprite.rect.y = 100
	elif sprite.rect.y >=600:
		sprite.rect.y =500

	screen.fill((255,255,255))

	all_sprites.update()
	
	
	all_sprites.draw(screen)

	pygame.display.flip()
pygame.QUIT