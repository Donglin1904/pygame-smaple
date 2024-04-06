import pygame
import random
from pygame.sprite import Sprite

class Enemy(Sprite):

	def __init__(self,main):
		super().__init__()
		self.screen=main.screen
		self.set=main.set
		self.enemy_life=self.set.enemy_life

		self.image=pygame.image.load('D:/python/fight/enemy.bmp')
		self.rect=self.image.get_rect()

		self.randint_number=random.randrange(self.rect.width,self.set.screen_width,self.rect.width)

		self.rect.x=self.randint_number
		self.rect.y=self.rect.height
		
	def update_enemy(self):
		self.rect.y += self.set.enemy_speed

class LeftEnemy(Sprite):

	def __init__(self,main):
		super().__init__()
		self.screen=main.screen
		self.set=main.set
		self.enemy_life=self.set.enemy_life

		self.image=pygame.image.load('D:/python/fight/enemy.bmp')
		self.rect=self.image.get_rect()

		self.randint_number=random.randrange(self.rect.height,self.set.screen_height,self.rect.height)

		self.rect.y=self.randint_number
		self.rect.x=self.rect.width

	def update_enemy_left(self):
		self.rect.x += self.set.enemy_speed





		