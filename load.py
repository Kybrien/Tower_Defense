import pygame as pg
import json
import constants as c

# Charge les "Addons"
pg.init()
pg.mixer.init() 
pg.font.init()
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT ))

# Map
map_image = pg.image.load('levels/level.png').convert_alpha()

# Turret spritesheets
turret_spritesheets = []
for x in range(1, c.TURRET_LEVELS + 1):
  turret_sheet = pg.image.load(f'assets/images/turrets/turret_{x}.png').convert_alpha()
  turret_spritesheets.append(turret_sheet)

# Image pour curseur
cursor_turret = pg.image.load('assets/images/turrets/cursor_turret.png').convert_alpha()

# ENEMIES
enemy_images = {
  "weak": pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha(),
  "medium": pg.image.load('assets/images/enemies/enemy_2.png').convert_alpha(),
  "strong": pg.image.load('assets/images/enemies/enemy_3.png').convert_alpha(),
  "elite": pg.image.load('assets/images/enemies/enemy_4.png').convert_alpha()
}
# BUTTONS
buy_turret_image = pg.image.load('assets/images/buttons/buy_turret.png').convert_alpha()
cancel_image = pg.image.load('assets/images/buttons/cancel.png').convert_alpha()
upgrade_turret_image = pg.image.load('assets/images/buttons/upgrade_turret.png').convert_alpha()
begin_image = pg.image.load('assets/images/buttons/begin.png').convert_alpha()
restart_image = pg.image.load('assets/images/buttons/restart.png').convert_alpha()
fast_forward_image = pg.image.load('assets/images/buttons/fast_forward.png').convert_alpha()
cancel_menu_image = pg.image.load('assets/images/buttons/cancel_menu.png').convert_alpha()

# GUI
heart_image = pg.image.load("assets/images/gui/heart.png").convert_alpha()
coin_image = pg.image.load("assets/images/gui/coin.png").convert_alpha()
logo_image = pg.image.load("assets/images/gui/logo.png").convert_alpha()

# Charge la musique et les effets sonores
shot_fx = pg.mixer.Sound('assets/audio/shot.wav')
shot_fx.set_volume(0.3)
button_sound = pg.mixer.Sound('assets/audio/button_effect.wav')
button_sound.set_volume(0.5)

music_background = pg.mixer.music.load('assets/audio/music_background.mp3')
pg.mixer.music.play(-1)  # L'argument -1 fait jouer la musique en boucle indéfiniment

# Ajustement du volume des effets sonores
def adjust_sound_effects_volume(volume):
  shot_fx.set_volume(volume)
  button_sound.set_volume(volume)
  if music_background is not None:
    music_background.set_volume(volume)

# Charge les Json Datas pour le Niveau
with open('levels/level.tmj') as file:
  world_data = json.load(file)

# Charge la Police
text_font = pg.font.SysFont("ebrima", 24, bold = True)
large_font = pg.font.SysFont("leelawadeeui", 36)
