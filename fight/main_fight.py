import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet,SuperBullet
from enemy import Enemy,LeftEnemy
from play_button import Button
from score import Score

class MainFight:

	def __init__(self):
		pygame.init()
		self.set=Settings()

		self.screen=pygame.display.set_mode((self.set.screen_width,self.set.screen_height))
		pygame.display.set_caption('ship fighting')

		self.ship=Ship(self)
		self.bullet=pygame.sprite.Group()
		self.super_bullet=pygame.sprite.Group()
		self.enemy=pygame.sprite.Group()
		self.left_enemy=pygame.sprite.Group()

		self.active=False
		self.button=Button(self,'Play')

		self.ship_life=self.set.ship_life
		self.get_ship_life_start=True
		self.ship_life_add_start='None'

		self.super_bullet_time=True
		self.super_bullet_start='None'

	def run_game(self):
		while True:
			self._check_event()
			self._update_screen()
			if self.active:
				self.bullet.update()
				self.ship.update()
				self.again_enemy()
				self._del_bullet()
				self._del_enemy()

	def _check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				elif event.key == pygame.K_w:
					self.ship.ship_up=True
				elif event.key == pygame.K_s:
					self.ship.ship_down=True
				elif event.key == pygame.K_a:
					self.ship.ship_left=True
				elif event.key == pygame.K_d:
					self.ship.ship_right=True
				elif event.key == pygame.K_SPACE:
					if len(self.bullet) < self.set.bullet_number:
						self._fire_bullet()
				elif event.key == pygame.K_f:
					self.ship_life_add()
				elif event.key == pygame.K_r:
					if self.super_bullet_time == False:
						if self.set.super_bullet_number>0:
							self._fire_super_bullet()
							self.set.super_bullet_number-=1
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					self.ship.ship_up=False
				elif event.key == pygame.K_s:
					self.ship.ship_down=False
				elif event.key == pygame.K_a:
					self.ship.ship_left=False
				elif event.key == pygame.K_d:
					self.ship.ship_right=False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos=pygame.mouse.get_pos()
				if self.button.rect.collidepoint(mouse_pos):
					self.active=True
					pygame.mouse.set_visible(False)

	def check_enemy_bullet(self):
		enemy_bullet=pygame.sprite.groupcollide(self.bullet,self.enemy,True,False)
		left_enemy_bullet=pygame.sprite.groupcollide(self.bullet,self.left_enemy,True,False)
		for enemys in enemy_bullet.values():
			for enemy in self.enemy.copy():
				if enemy in enemys:
					enemy.enemy_life-=self.set.bullet_attack
					if enemy.enemy_life <= 0:
						self.enemy.remove(enemy)
						self.set.score+=self.set.score_add
		for enemys in left_enemy_bullet.values():
			for left_enemy in self.left_enemy.copy():
				if left_enemy in enemys:
					left_enemy.enemy_life-=self.set.bullet_attack
					if left_enemy.enemy_life <= 0:
						self.left_enemy.remove(left_enemy)
						self.set.score+=self.set.score_add

	def check_enemy_ship(self):
		for enemy in self.enemy.copy():
			if pygame.sprite.collide_rect(self.ship,enemy) == True:
				self.enemy.remove(enemy)
				self.ship_life -= self.set.enemy_attack
		for left_enemy in self.left_enemy.copy():
			if pygame.sprite.collide_rect(self.ship,left_enemy) == True:
				self.left_enemy.remove(left_enemy)
				self.ship_life -= self.set.enemy_attack
		if self.ship_life <= 0:
			self.active=False

	def check_enemy_superbullet(self):
		for enemy in self.enemy.copy():
			for bullet in self.super_bullet.copy():
				if pygame.sprite.collide_rect(enemy,bullet):
					self.enemy.remove(enemy)
					self.set.score+=self.set.super_bullet_score
		for enemy in self.left_enemy.copy():
			for bullet in self.super_bullet.copy():
				if pygame.sprite.collide_rect(enemy,bullet):
					self.left_enemy.remove(enemy)
					self.set.score+=self.set.super_bullet_score			

	def _fire_bullet(self):
		new_bullet=Bullet(self)
		self.bullet.add(new_bullet)

	def _fire_super_bullet(self):
		new_bullet=SuperBullet(self)
		self.super_bullet.add(new_bullet)

	def add_enemy(self):
		new_enemy=Enemy(self)
		self.enemy.add(new_enemy)

	def add_enemy_left(self):
		new_left_enemy=LeftEnemy(self)
		self.left_enemy.add(new_left_enemy)

	def _del_bullet(self):
		for bullet in self.bullet.copy():
			if bullet.rect.bottom <= 0:
				self.bullet.remove(bullet)

	def _del_super_bullet(self):
		for bullet in self.super_bullet.copy():
			if bullet.rect.right <= 0:
				self.super_bullet.remove(bullet)

	def _draw_enemy(self):
		self.enemy.draw(self.screen)

	def _draw_enemy_left(self):
		self.left_enemy.draw(self.screen)

	def _del_enemy(self):
		for enemy in self.enemy.copy():
			if enemy.rect.bottom >= self.set.screen_height:
				self.enemy.remove(enemy)
		for left_enemy in self.left_enemy.copy():
			if left_enemy.rect.right >= self.set.screen_width:
				self.left_enemy.remove(left_enemy)

	def again_enemy(self):
		if len(self.enemy) == 0:
			for i in range(self.set.enemy_again):
				self.add_enemy()
		if len(self.left_enemy) == 0:
			for a in range(self.set.enemy_again):
				self.add_enemy_left()

	def update_score(self):
		self.score=Score(self)
		self.score.draw_score()

	def ship_life_add(self):
		if self.ship_life_add_start != 'None':
			if self.ship_life_add_cd >= self.set.ship_life_add_cd:
				if self.ship_life <= 15:
					self.ship_life += self.set.ship_life_add
				else:
					self.ship_life=20	
				self.ship_life_add_start=pygame.time.get_ticks()			

	def score_add_plus(self):
		if self.set.score <=500:
			self.set.score_add=30
			self.set.enemy_again=1
			self.set.enemy_life=1
			self.set.enemy_speed=2
			self.set.enemy_attack=1
		elif 500< self.set.score <=1500:
			self.set.score_add=60
			self.set.enemy_again=2
			self.set.enemy_life=1
			self.set.bullet_number=3
		elif 1500< self.set.score <=3500:
			self.set.score_add=120
			self.set.enemy_again=3
			self.set.enemy_life=2
			self.set.bullet_number=5
		elif 3500< self.set.score <=6000:
			self.set.score_add=150
			self.set.enemy_again=4
			self.set.enemy_attack=2
			self.set.enemy_life=2
		else:
			self.set.score_add=200
			self.set.enemy_again=4
			self.set.enemy_life=3
			self.set.enemy_speed=3
			self.set.enemy_attack=3
			self.set.bullet_number=10
		if self.set.score >= 500 and self.get_ship_life_start:
			self.ship_life_add_start=pygame.time.get_ticks()
			self.get_ship_life_start=False
		if self.set.score >= 1000 and self.super_bullet_time:
			self.super_bullet_start=pygame.time.get_ticks()
			self.set.super_bullet_number=3
			self.super_bullet_time=False

	def _update_ship_life_cd(self):
		if self.ship_life_add_start != 'None':
			self.ship_life_add_end=pygame.time.get_ticks()
			self.ship_life_add_cd=self.ship_life_add_end - self.ship_life_add_start
			self.ship_life_add_cd=round(self.ship_life_add_cd,-3)/1000
			if self.ship_life_add_cd >= self.set.ship_life_add_cd:
				self.ship_life_add_wait=0
			else:
				self.ship_life_add_wait=float(self.set.ship_life_add_cd-self.ship_life_add_cd)
		else:
			self.ship_life_add_wait='None'

	def _update_super_bullet_cd(self):
		if self.super_bullet_start != 'None':
			if self.set.super_bullet_number != 'None':
				if self.set.super_bullet_number < 3:
					self.super_bullet_end=pygame.time.get_ticks()
					self.super_bullet_cd=self.super_bullet_end - self.super_bullet_start
					self.super_bullet_cd=round(self.super_bullet_cd,-3)/1000
					if self.super_bullet_cd >= self.set.super_bullet_cd:
						self.set.super_bullet_number+=1
						self.super_bullet_start=pygame.time.get_ticks()
					else:
						self.super_bullet_wait=float(self.set.super_bullet_cd-self.super_bullet_cd)
				elif self.set.super_bullet_number == 3:
					self.set.super_bullet_number=3
					self.super_bullet_wait=0
		else:
			self.super_bullet_wait='None'

	def _update_screen(self):
		self.screen.fill(self.set.screen_colour)
		self.score_add_plus()
		self._update_ship_life_cd()
		self._update_super_bullet_cd()
		self.update_score()
		self._del_super_bullet()
		if not self.active:
			self.enemy.empty()
			self.left_enemy.empty()
			self.bullet.empty()
			self.super_bullet.empty()
			pygame.mouse.set_visible(True)		
			self.ship.rect.midbottom=self.screen.get_rect().midbottom
			self.ship_life=self.set.ship_life
			self.button.draw_button()
			if int(self.score.high_score) < int(self.set.score):
				with open('D:/python/fight/high_score.txt','w') as high_score:
					high_score.write(str(self.set.score))
			self.set.score=0
			self.set.ship_life=20
			self.set.bullet_number=2
			self.set.super_bullet_number='None'
			self.super_bullet_start='None'
			self.ship_life_add_start='None'
			self.get_ship_life_start=True
			self.super_bullet_time=True
		self.check_enemy_ship()
		self.check_enemy_bullet()
		self.check_enemy_superbullet()
		self.ship.blitme()

		for bullet in self.bullet.sprites():
			bullet.draw_bullet()
		for bullet in self.super_bullet.sprites():
			bullet.draw_super_bullet()
			bullet.update_super_bullet()

		for enemy in self.enemy.sprites():
			self._draw_enemy()
			enemy.update_enemy()
		for left_enemy in self.left_enemy.sprites():
			self._draw_enemy_left()
			left_enemy.update_enemy_left()

		pygame.display.flip()

if __name__ == '__main__':
	ai=MainFight()
	ai.run_game()
