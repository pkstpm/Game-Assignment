import pygame 
from settings import *
from tile import Tile
from player import Player
from support import *
from debug import *
from weapon import Weapon
from ui import UI
from enemy import Enemy

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# user interface
		self.ui = UI()

	def create_map(self):
		layout = {
			'boundary' : import_csv_layout('maps/maps_Sea.csv'),
			'object' : import_csv_layout('maps/maps_Object.csv'),
			'entities' : import_csv_layout('maps/maps_entities.csv')
		}
		for style,layout in layout.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible')
						if style == 'object':
							Tile((x,y),[self.obstacle_sprites],'object')
						if style == 'entities':
							if col == '17':
								self.player = Player(
									(x,y),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.create_skill)
							else:
								if col == '65': monster_name = 'demon'
								elif col == '59': monster_name = 'pirate'
								elif col == '54': monster_name = 'orc'
								else: monster_name = 'dragon'
								Enemy(monster_name,(x,y),[self.visible_sprites],self.obstacle_sprites)
		
	def create_attack(self):
		Weapon(self.player,[self.visible_sprites])

	def create_skill(self,style,strength,cost):
		print(style)
		print(strength)
		print(cost)

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.visible_sprites.enemy_update(self.player)
		self.ui.display(self.player)

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		#creating floor
		self.floor_surf = pygame.image.load('graphics/maps.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		#drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

	def enemy_update(self,player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)
