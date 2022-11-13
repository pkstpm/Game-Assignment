import pygame
from settings import *
from entity import Entity

class Enemy(Entity):
    def __init__(self,monster_name,pos,groups,obstacle_sprites):

        #general setup
        super().__init__(groups)
        self.spirte_type = 'enemy'

        #graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        #movement
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacle_sprites = obstacle_sprites

        #stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        # player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

    def import_graphics(self,name):
        if name == 'demon':
            demon_down0 = pygame.image.load('graphics/monsters/demon/move/down0.png').convert_alpha()
            demon_down1 = pygame.image.load('graphics/monsters/demon/move/down1.png').convert_alpha()
            demon_down2 = pygame.image.load('graphics/monsters/demon/move/down2.png').convert_alpha()            
            demon_down3 = pygame.image.load('graphics/monsters/demon/move/down3.png').convert_alpha()
            demon_down4 = pygame.image.load('graphics/monsters/demon/move/down4.png').convert_alpha()
            demon_attack0 = pygame.image.load('graphics/monsters/demon/attack/down_attack0.png').convert_alpha()
            demon_attack1 = pygame.image.load('graphics/monsters/demon/attack/down_attack1.png').convert_alpha()
            demon_attack2 = pygame.image.load('graphics/monsters/demon/attack/down_attack2.png').convert_alpha()
            demon_attack3 = pygame.image.load('graphics/monsters/demon/attack/down_attack3.png').convert_alpha()
            demon_attack4 = pygame.image.load('graphics/monsters/demon/attack/down_attack4.png').convert_alpha()
            demon_attack5 = pygame.image.load('graphics/monsters/demon/attack/down_attack5.png').convert_alpha()

            self.animations = {'idle' : [demon_down0,demon_down1] ,
                'move' : [demon_down0,demon_down1,demon_down2,demon_down3,demon_down4],
                'attack' : [demon_attack0,demon_attack1,demon_attack2,demon_attack3,demon_attack4,demon_attack5]}
        if name == 'pirate':
            pirate_down0 = pygame.image.load('graphics/monsters/pirate/move/down0.png').convert_alpha()
            pirate_down1 = pygame.image.load('graphics/monsters/pirate/move/down1.png').convert_alpha()
            pirate_down2 = pygame.image.load('graphics/monsters/pirate/move/down2.png').convert_alpha()            
            pirate_down3 = pygame.image.load('graphics/monsters/pirate/move/down3.png').convert_alpha()
            pirate_down4 = pygame.image.load('graphics/monsters/pirate/move/down4.png').convert_alpha()
            pirate_attack0 = pygame.image.load('graphics/monsters/pirate/attack/down_attack0.png').convert_alpha()
            pirate_attack1 = pygame.image.load('graphics/monsters/pirate/attack/down_attack1.png').convert_alpha()
            pirate_attack2 = pygame.image.load('graphics/monsters/pirate/attack/down_attack2.png').convert_alpha()
            pirate_attack3 = pygame.image.load('graphics/monsters/pirate/attack/down_attack3.png').convert_alpha()

            self.animations = {'idle' : [pirate_down0,pirate_down1] ,
                'move' : [pirate_down0,pirate_down1,pirate_down2,pirate_down3,pirate_down4],
                'attack' : [pirate_attack0,pirate_attack1,pirate_attack2,pirate_attack3]}
        if name == 'orc':
            orc_down0 = pygame.image.load('graphics/monsters/orc/move/down0.png').convert_alpha()
            orc_down1 = pygame.image.load('graphics/monsters/orc/move/down1.png').convert_alpha()
            orc_down2 = pygame.image.load('graphics/monsters/orc/move/down2.png').convert_alpha()            
            orc_down3 = pygame.image.load('graphics/monsters/orc/move/down3.png').convert_alpha()
            orc_down4 = pygame.image.load('graphics/monsters/orc/move/down4.png').convert_alpha()
            orc_attack0 = pygame.image.load('graphics/monsters/orc/attack/down_attack0.png').convert_alpha()
            orc_attack1 = pygame.image.load('graphics/monsters/orc/attack/down_attack1.png').convert_alpha()
            orc_attack2 = pygame.image.load('graphics/monsters/orc/attack/down_attack2.png').convert_alpha()
            orc_attack3 = pygame.image.load('graphics/monsters/orc/attack/down_attack3.png').convert_alpha()
            orc_attack4 = pygame.image.load('graphics/monsters/orc/attack/down_attack4.png').convert_alpha()
            orc_attack5 = pygame.image.load('graphics/monsters/orc/attack/down_attack5.png').convert_alpha()

            self.animations = {'idle' : [orc_down0,orc_down1] ,
                'move' : [orc_down0,orc_down1,orc_down2,orc_down3,orc_down4],
                'attack' : [orc_attack0,orc_attack1,orc_attack2,orc_attack3,orc_attack4,orc_attack5]}
        if name == 'dragon':
            dragon_down0 = pygame.image.load('graphics/monsters/dragon/move/down0.png').convert_alpha()
            dragon_down1 = pygame.image.load('graphics/monsters/dragon/move/down1.png').convert_alpha()
            dragon_down2 = pygame.image.load('graphics/monsters/dragon/move/down2.png').convert_alpha()            
            dragon_down3 = pygame.image.load('graphics/monsters/dragon/move/down3.png').convert_alpha()
            dragon_attack0 = pygame.image.load('graphics/monsters/dragon/attack/down_attack0.png').convert_alpha()
            dragon_attack1 = pygame.image.load('graphics/monsters/dragon/attack/down_attack1.png').convert_alpha()

            self.animations = {'idle' : [dragon_down0] ,
                'move' : [dragon_down0,dragon_down1,dragon_down2,dragon_down3],
                'attack' : [dragon_attack0,dragon_attack1]}

    def get_player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance,direction)

    def get_status(self,player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius:
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self,player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            print('attack')
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate(self):
        animation = self.animations[self.status]
		
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def update(self):
        self.move(self.speed)
        self.animate()
        self.cooldown()

    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)