import pygame as pg
import constants as c
from button import Button
# from world import World
# import world
import load

# Créer la fenêtre et retourner l'objet screen
def create_window():
    screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
    pg.display.set_caption("Cower Defense")
    return screen

# Afficher le texte à l'écran
def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Creer la Map
# def create_world() :
#   world = World(load.world_data, load.map_image)
#   world.process_data()
#   world.process_enemies()

# Creer les Boutons
def create_buttons():
    buttons = {
        'turret_button': Button(c.SCREEN_WIDTH + 5, 120, load.buy_turret_image, True),
        'cancel_button': Button(c.SCREEN_WIDTH + 45, 180, load.cancel_image, True),
        'upgrade_button': Button(c.SCREEN_WIDTH + 5, 180, load.upgrade_turret_image, True),
        'begin_button': Button(c.SCREEN_WIDTH + 60, 300, load.begin_image, True),
        'restart_button': Button(250, 300, load.restart_image, True),
        'fast_forward_button': Button(c.SCREEN_WIDTH + 80, 300, load.fast_forward_image, False),
        'cancel_menu_button': Button(c.SCREEN_WIDTH + 175, 10, load.cancel_menu_image, True),    }
    return buttons

def display_data(screen,world) :
  # Affiche un rectangle
  pg.draw.rect(screen, ((50,50,50)), (c.SCREEN_WIDTH, 0, c.SIDE_PANEL, c.SCREEN_HEIGHT))
  pg.draw.rect(screen, "grey0", (c.SCREEN_WIDTH, 0, c.SIDE_PANEL, 400), 2)
  screen.blit(load.logo_image, (c.SCREEN_WIDTH, 400))
  #Affiche les Datas
  draw_text(screen, "Niveau: " + str(world.level), load.text_font, "grey100", c.SCREEN_WIDTH + 10, 10)
  screen.blit(load.heart_image, (c.SCREEN_WIDTH + 10, 35))
  draw_text(screen, str(world.health), load.text_font, "grey100", c.SCREEN_WIDTH + 50, 40)
  screen.blit(load.coin_image, (c.SCREEN_WIDTH + 10, 65))
  draw_text(screen, str(world.money), load.text_font, "grey100", c.SCREEN_WIDTH + 50, 70)
