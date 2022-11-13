import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        self.frame_index = 0
        direction = player.status.split('_')[0]

        # graphic
        self.image = pygame.Surface((16,16))
        self.rect = self.image.get_rect(center = player.rect.center)
       
        cut0 = pygame.image.load('graphics/particles/cut/cut_0.png').convert_alpha
        cut1 = pygame.image.load('graphics/particles/cut/cut_1.png').convert_alpha
        cut2 = pygame.image.load('graphics/particles/cut/cut_2.png').convert_alpha
        cut3 = pygame.image.load('graphics/particles/cut/cut_3.png').convert_alpha
        cut4 = pygame.image.load('graphics/particles/cut/cut_4.png').convert_alpha
        cut5 = pygame.image.load('graphics/particles/cut/cut_5.png').convert_alpha
        self.cut = [cut0,cut1,cut2,cut3,cut4,cut5]
            
        # placement
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright)
        elif direction == 'left': 
            self.rect = self.image.get_rect(midright = player.rect.midleft)
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)
        else:
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)