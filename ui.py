import pygame
from settings import *

class UI:
    def __init__(self):
        
        #general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,ui_font_size)

        #bar setup
        self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)

        #convert skill dictionary
        self.skill_graphics = []
        for skill in skill_data.values():
            skill = pygame.image.load(skill['graphic']).convert_alpha()
            self.skill_graphics.append(skill)

    def show_bar(self,current,max_amount,bg_rect,color):
        #draw bg
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

        # converting stat to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # drawing the bar
        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)

    def selection_box(self,left,top,has_switched):
        bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rect,3)
        else:
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
        return bg_rect

    def skill_over_lay(self,skill_index,has_switched):
        bg_rect = self.selection_box(10,630,has_switched)
        skill_surf = self.skill_graphics[skill_index]
        skill_rect = skill_surf.get_rect(center = bg_rect.center)

        self.display_surface.blit(skill_surf,skill_rect)

    def display(self,player):
        self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)
        self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,ENERGY_COLOR)

        self.skill_over_lay(player.skill_index,not player.can_switch_skill)