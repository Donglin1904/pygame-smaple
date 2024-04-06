import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self,main):
		super().__init__()
		self.screen=main.screen
		self.set=main.set
		self.colour=self.set.bullet_colour

		self.rect=pygame.Rect(0,0,self.set.bullet_width,self.set.bullet_height)
		self.rect.midtop=main.ship.rect.midtop

	def update(self):
		self.rect.y -= self.set.bullet_speed

	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.colour,self.rect)

class SuperBullet(Sprite):

	def __init__(self,main):
		super().__init__()
		self.screen=main.screen
		self.set=main.set
		self.colour=self.set.bullet_colour

		self.rect=pygame.Rect(0,0,self.set.super_bullet_width,self.set.super_bullet_height)
		self.rect.right=main.ship.rect.left

	def update_super_bullet(self):
		self.rect.x -= self.set.super_bullet_speed

	def draw_super_bullet(self):
		pygame.draw.rect(self.screen,self.colour,self.rect)

