class Settings:
	
	def __init__(self):
		#修改时main.py update_screen中还有需修改值
		self.screen_width=1200
		self.screen_height=650
		self.screen_colour=(230,230,230)

		self.ship_speed=2
		self.ship_life=20
		self.ship_life_add=5
		self.ship_life_add_cd=14

		self.bullet_speed=2
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_colour=(60,60,60)
		self.bullet_attack=1
		self.bullet_number=2

		self.super_bullet_width=10
		self.super_bullet_height=self.screen_height
		self.super_bullet_speed=4
		self.super_bullet_number='None'
		self.super_bullet_score=20
		self.super_bullet_cd=9

		self.enemy_speed=2
		self.enemy_again=1
		self.enemy_life=1
		self.enemy_attack=1

		self.score=0
		self.score_add=30
