import pygame 
from settings import *
from entity import Entity

class Player(Entity):
	def __init__(self,pos,groups,obstacle_sprites,create_attack,create_skill):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/player/down/down_1.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-5)

		down0 = pygame.image.load('graphics/player/down_idle/down_idle.png').convert_alpha()
		down1 = pygame.image.load('graphics/player/down/down_1.png').convert_alpha()
		down2 = pygame.image.load('graphics/player/down/down_2.png').convert_alpha()
		down3 = pygame.image.load('graphics/player/down/down_3.png').convert_alpha()
		down4 = pygame.image.load('graphics/player/down/down_4.png').convert_alpha()

		up0 = pygame.image.load('graphics/player/up_idle/up_idle.png').convert_alpha()
		up1 = pygame.image.load('graphics/player/up/up_1.png').convert_alpha()
		up2 = pygame.image.load('graphics/player/up/up_2.png').convert_alpha()
		up3 = pygame.image.load('graphics/player/up/up_3.png').convert_alpha()
		up4 = pygame.image.load('graphics/player/up/up_4.png').convert_alpha()

		right0 = pygame.image.load('graphics/player/right_idle/right_idle.png').convert_alpha()
		right1 = pygame.image.load('graphics/player/right/right_1.png').convert_alpha()
		right2 = pygame.image.load('graphics/player/right/right_2.png').convert_alpha()
		right3 = pygame.image.load('graphics/player/right/right_3.png').convert_alpha()
		right4 = pygame.image.load('graphics/player/right/right_4.png').convert_alpha()

		left0 = pygame.image.load('graphics/player/left_idle/left_idle.png').convert_alpha()
		left1 = pygame.image.load('graphics/player/left/left_1.png').convert_alpha()
		left2 = pygame.image.load('graphics/player/left/left_2.png').convert_alpha()
		left3 = pygame.image.load('graphics/player/left/left_3.png').convert_alpha()
		left4 = pygame.image.load('graphics/player/left/left_4.png').convert_alpha()

		down_attack1 = pygame.image.load('graphics/player/down_attack/down_attack_1.png').convert_alpha()
		down_attack2 = pygame.image.load('graphics/player/down_attack/down_attack_2.png').convert_alpha()
		down_attack3 = pygame.image.load('graphics/player/down_attack/down_attack_3.png').convert_alpha()
		down_attack4 = pygame.image.load('graphics/player/down_attack/down_attack_4.png').convert_alpha()
		down_attack5 = pygame.image.load('graphics/player/down_attack/down_attack_5.png').convert_alpha()
		down_attack6 = pygame.image.load('graphics/player/down_attack/down_attack_6.png').convert_alpha()

		up_attack1 = pygame.image.load('graphics/player/up_attack/up_attack_1.png').convert_alpha()
		up_attack2 = pygame.image.load('graphics/player/up_attack/up_attack_2.png').convert_alpha()
		up_attack3 = pygame.image.load('graphics/player/up_attack/up_attack_3.png').convert_alpha()
		up_attack4 = pygame.image.load('graphics/player/up_attack/up_attack_4.png').convert_alpha()
		up_attack5 = pygame.image.load('graphics/player/up_attack/up_attack_5.png').convert_alpha()
		up_attack6 = pygame.image.load('graphics/player/up_attack/up_attack_6.png').convert_alpha()

		right_attack1 = pygame.image.load('graphics/player/right_attack/right_attack_1.png').convert_alpha()
		right_attack2 = pygame.image.load('graphics/player/right_attack/right_attack_2.png').convert_alpha()
		right_attack3 = pygame.image.load('graphics/player/right_attack/right_attack_3.png').convert_alpha()
		right_attack4 = pygame.image.load('graphics/player/right_attack/right_attack_4.png').convert_alpha()
		right_attack5 = pygame.image.load('graphics/player/right_attack/right_attack_5.png').convert_alpha()
		right_attack6 = pygame.image.load('graphics/player/right_attack/right_attack_6.png').convert_alpha()

		left_attack1 = pygame.image.load('graphics/player/left_attack/left_attack_1.png').convert_alpha()
		left_attack2 = pygame.image.load('graphics/player/left_attack/left_attack_2.png').convert_alpha()
		left_attack3 = pygame.image.load('graphics/player/left_attack/left_attack_3.png').convert_alpha()
		left_attack4 = pygame.image.load('graphics/player/left_attack/left_attack_4.png').convert_alpha()
		left_attack5 = pygame.image.load('graphics/player/left_attack/left_attack_5.png').convert_alpha()
		left_attack6 = pygame.image.load('graphics/player/left_attack/left_attack_6.png').convert_alpha()

		self.animations = {'up': [up1,up2,up3,up4],'down': [down1,down2,down3,down4],'left': [left1,left2,left3,left4],'right': [right1,right2,right3,right4],
			'right_idle':[right0,right1],'left_idle':[left0,left1],'up_idle':[up0,up1],'down_idle':[down0,down1],
			'right_attack':[right_attack1,right_attack2,right_attack3,right_attack4,right_attack5,right_attack6],
			'left_attack':[left_attack1,left_attack2,left_attack3,left_attack4,left_attack5,left_attack6],
			'up_attack':[up_attack1,up_attack2,up_attack3,up_attack4,up_attack5,up_attack6],
			'down_attack':[down_attack1,down_attack2,down_attack3,down_attack4,down_attack5,down_attack6]}

		#graphics setup
		self.status = 'down'

		#movement
		self.speed = 5
		self.attacking = False
		self.attack_cooldown = 600
		self.attack_time = None
		self.obstacle_sprites = obstacle_sprites

		#attack
		self.create_attack = create_attack
		
		#skill
		self.create_skill = create_skill
		self.skill_index = 0
		self.skill = list(skill_data.keys())[self.skill_index]
		self.can_switch_skill = True
		self.skill_switch_time = None
		self.switch_duration_cooldown = 200

		# stats
		self.stats = {'health' : 100 , 'energy' : 60 , 'attack' : 10 , 'magic' : 4 , 'speed' : 6}
		self.health = self.stats['health']
		self.energy = self.stats['energy']
		self.speed = self.stats['speed']

	def input(self):
		if not self.attacking:
			keys = pygame.key.get_pressed()

			if keys[pygame.K_UP]:
				#self.up_animation()
				self.direction.y = -1
				self.status = 'up'
			elif keys[pygame.K_DOWN]:
				#self.down_animation()
				self.direction.y = 1
				self.status = 'down'
			else:
				self.direction.y = 0

			if keys[pygame.K_RIGHT]:
				#.right_animation()
				self.direction.x = 1
				self.status = 'right'
			elif keys[pygame.K_LEFT]:
				#self.left_animation()
				self.direction.x = -1
				self.status = 'left'
			else:
				self.direction.x = 0

			#attack input
			if keys[pygame.K_a]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				self.create_attack()

			#skiil input
			if keys[pygame.K_d]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				style = list(skill_data.keys())[self.skill_index]
				strength = list(skill_data.values())[self.skill_index]['strength'] + self.stats['magic']
				cost = list(skill_data.values())[self.skill_index]['cost']
				self.create_skill(style,strength,cost)

			if keys[pygame.K_s] and self.can_switch_skill:
				self.can_switch_skill = False
				self.skill_switch_time = pygame.time.get_ticks()

				if self.skill_index < len(list(skill_data.keys())) - 1:
					self.skill_index += 1
				else:
					self.skill_index = 0

				self.skill = list(skill_data.keys())[self.skill_index]

	def get_status(self):

		#idle status
		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status and not 'attack' in self.status:
				self.status = self.status + '_idle'

		if self.attacking:
			self.direction.x = 0
			self.direction.y = 0
			if not 'attack' in self.status:
				if 'idle' in self.status:
					self.status = self.status.replace('_idle','_attack')
				else:
					self.status = self.status + '_attack'
		else:
			if 'attack' in self.status:
				self.status = self.status.replace('_attack','')

	def cooldowns(self):
		current_time = pygame.time.get_ticks()

		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.attacking = False

		if not self.can_switch_skill:
			if current_time - self.skill_switch_time >= self.switch_duration_cooldown:
				self.can_switch_skill = True

	def animate(self):
			animation = self.animations[self.status]

			# loop over the frame index 
			self.frame_index += self.animation_speed
			if self.frame_index >= len(animation):
				self.frame_index = 0

			# set the image
			self.image = animation[int(self.frame_index)]
			self.rect = self.image.get_rect(center = self.hitbox.center)

	def update(self):
		self.input()
		self.cooldowns()
		self.get_status()
		self.animate()
		self.move(self.speed)