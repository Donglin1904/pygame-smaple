import pygame
from settings import Settings

class Ship:

	def __init__(self,main):
		self.screen=main.screen
		self.screen_rect=main.screen.get_rect()

		self.image=pygame.image.load('D:/python/fight/ship.bmp')
		self.rect=self.image.get_rect()

		self.rect.midbottom=self.screen_rect.midbottom

		self.ship_right=False
		self.ship_left=False
		self.ship_up=False
		self.ship_down=False

		self.set=Settings()

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update(self):
		if self.ship_right and self.rect.right < self.screen_rect.right:
			self.rect.x += self.set.ship_speed
		if self.ship_left and self.rect.left > 0:
			self.rect.x -= self.set.ship_speed
		if self.ship_up and self.rect.top > 0:
			self.rect.y -= self.set.ship_speed
		if self.ship_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += self.set.ship_speed



