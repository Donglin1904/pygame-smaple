import pygame
from settings import Settings

class Score:

	def __init__(self,main):
		self.screen=main.screen
		self.screen_rect=main.screen.get_rect()
		self.set=main.set

		self.score=self.set.score
		self.ship_life=main.ship_life
		self.ship_life_wait=main.ship_life_add_wait

		self.super_bullet_wait=main.super_bullet_wait
		self.super_bullet_number=self.set.super_bullet_number

		self.text_colour=(30,30,30)
		self.font=pygame.font.SysFont(None,48)

		self._prep_score()
		self._prep_ship_life()
		self._prep_ship_life_cd()
		self._prep_super_bullet_cd()
		self._prep_super_bullet_number()

		with open('D:/python/fight/high_score.txt','r') as high_score:
			self.high_score=high_score.read()
		self._prep_high_score()

	def _prep_score(self):
		score=str(self.score)
		score=f'Score:{score}'
		self.score_image=self.font.render(score,True,self.text_colour,self.set.screen_colour)
		self.score_image_rect=self.score_image.get_rect()
		self.score_image_rect.right=self.screen_rect.right-20
		self.score_image_rect.top=20

	def _prep_ship_life(self):
		ship_life=str(self.ship_life)
		ship_life=f'Life:{ship_life}'
		self.ship_life_image=self.font.render(ship_life,True,self.text_colour,self.set.screen_colour)
		self.ship_life_image_rect=self.ship_life_image.get_rect()
		self.ship_life_image_rect.right=self.screen_rect.right-20
		self.ship_life_image_rect.top=self.score_image_rect.bottom+10

	def _prep_high_score(self):
		high_score=str(self.high_score)
		high_score=f'High Score:{high_score}'
		self.high_score_image=self.font.render(high_score,True,self.text_colour,self.set.screen_colour)
		self.high_score_image_rect=self.high_score_image.get_rect()
		self.high_score_image_rect.midtop=self.screen_rect.midtop

	def _prep_ship_life_cd(self):
		ship_life_cd=str(self.ship_life_wait)
		ship_life_cd=f'ship life return.cd:{ship_life_cd}'
		self.ship_life_cd_image=self.font.render(ship_life_cd,True,
			self.text_colour,self.set.screen_colour)
		self.ship_life_cd_image_rect=self.ship_life_cd_image.get_rect()
		self.ship_life_cd_image_rect.right=self.screen_rect.right-20
		self.ship_life_cd_image_rect.top=self.ship_life_image_rect.bottom+10

	def _prep_super_bullet_cd(self):
		super_bullet_cd=str(self.super_bullet_wait)
		super_bullet_cd=f'Super bullet cd:{super_bullet_cd}'
		self.super_bullet_cd_image=self.font.render(super_bullet_cd,True,
			self.text_colour,self.set.screen_colour)
		self.super_bullet_cd_image_rect=self.super_bullet_cd_image.get_rect()
		self.super_bullet_cd_image_rect.right=self.screen_rect.right-20
		self.super_bullet_cd_image_rect.top=self.ship_life_cd_image_rect.bottom+10

	def _prep_super_bullet_number(self):
		super_bullet_number=str(self.super_bullet_number)
		super_bullet_number=f'Super bullet left:{super_bullet_number}'
		self.super_bullet_number_image=self.font.render(super_bullet_number,True,
			self.text_colour,self.set.screen_colour)
		self.super_bullet_number_image_rect=self.super_bullet_number_image.get_rect()
		self.super_bullet_number_image_rect.right=self.screen_rect.right-20
		self.super_bullet_number_image_rect.top=self.super_bullet_cd_image_rect.bottom+10

	def draw_score(self):
		self.screen.blit(self.score_image,self.score_image_rect)
		self.screen.blit(self.ship_life_image,self.ship_life_image_rect)
		self.screen.blit(self.high_score_image,self.high_score_image_rect)
		self.screen.blit(self.ship_life_cd_image,self.ship_life_cd_image_rect)
		self.screen.blit(self.super_bullet_cd_image,self.super_bullet_cd_image_rect)
		self.screen.blit(self.super_bullet_number_image,self.super_bullet_number_image_rect)
