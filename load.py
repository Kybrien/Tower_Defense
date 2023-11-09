import pygame as pg
import json
import constants as c

class Load:
    def __init__(self):
        pg.init()
        pg.mixer.init()

        # Load images
        self.map_image = pg.image.load('levels/level.png').convert_alpha()
        self.turret_spritesheets = []
        for x in range(1, c.TURRET_LEVELS + 1):
            turret_sheet = pg.image.load(f'assets/images/turrets/turret_{x}.png').convert_alpha()
            self.turret_spritesheets.append(turret_sheet)
        self.cursor_turret = pg.image.load('assets/images/turrets/cursor_turret.png').convert_alpha()
        self.enemy_images = {
            "weak": pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha(),
            "medium": pg.image.load('assets/images/enemies/enemy_2.png').convert_alpha(),
            "strong": pg.image.load('assets/images/enemies/enemy_3.png').convert_alpha(),
            "elite": pg.image.load('assets/images/enemies/enemy_4.png').convert_alpha()
        }
        self.buy_turret_image = pg.image.load('assets/images/buttons/buy_turret.png').convert_alpha()
        self.cancel_image = pg.image.load('assets/images/buttons/cancel.png').convert_alpha()
        self.upgrade_turret_image = pg.image.load('assets/images/buttons/upgrade_turret.png').convert_alpha()
        self.begin_image = pg.image.load('assets/images/buttons/begin.png').convert_alpha()
        self.restart_image = pg.image.load('assets/images/buttons/restart.png').convert_alpha()
        self.fast_forward_image = pg.image.load('assets/images/buttons/fast_forward.png').convert_alpha()
        self.heart_image = pg.image.load("assets/images/gui/heart.png").convert_alpha()
        self.coin_image = pg.image.load("assets/images/gui/coin.png").convert_alpha()
        self.logo_image = pg.image.load("assets/images/gui/logo.png").convert_alpha()

        # Load sounds
        self.shot_fx = pg.mixer.Sound('assets/audio/shot.wav')
        self.shot_fx.set_volume(0.5)

        # Load json data for level
        with open('levels/level.tmj') as file:
            self.world_data = json.load(file)

        # Load fonts for displaying text on the screen
        self.text_font = pg.font.SysFont("Consolas", 24, bold=True)
        self.large_font = pg.font.SysFont("Consolas", 36)

    def run(self):
        # Your game logic can go here
        pass

