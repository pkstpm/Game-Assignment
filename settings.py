# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 32

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'graphics/font/joystix.ttf'
ui_font_size = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

#weapon
weapon_data = {
    'sword' : { 'cooldown' : 100 , 'damage' : 20}
}

#skill
skill_data = {
    'flame': {'strength': 5,'cost': 20,'graphic':'graphics/particles/flame/fire.png'},
    'smoke' : {'strength': 2,'cost': 10,'graphic':'graphics/particles/smoke/smoke.png'},
    'heal' : {'strength': 20,'cost': 10,'graphic':'graphics/particles/heal/heal.png'}
}

#monster
monster_data = {
    'demon' :{'health': 100,'exp':100,'damage':20,'attack_type': 'claw', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'orc' : {'health': 300,'exp':250,'damage':40,'attack_type': 'claw', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'pirate' : {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'dragon' :{'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}