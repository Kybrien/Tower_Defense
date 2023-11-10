import pygame as pg
import constants as c
from world import World
from enemy import Enemy
from turret import Turret
import turret
import menu
import load
import display

WHITE = pg.Color(255, 255, 255)
BLACK = pg.Color(0, 0, 0)


def game_run() :
  #create clock
  clock = pg.time.Clock()
  
  # Variables de jeu
  game_over = False
  game_outcome = 0 # -1 is loss & 1 is win
  level_started = False
  last_enemy_spawn = pg.time.get_ticks()
  placing_turrets = False
  selected_turret = None
  wave_number = 0 
  boss_spawned = False 
  
  #create groups
  enemy_group = pg.sprite.Group()
  turret_group = pg.sprite.Group()
  
  
  
  # Créer la fenêtre
  screen = display.create_window()
  
  # Créer les boutons
  buttons = display.create_buttons()
  
  # Créer le monde
  world = World(load.world_data, load.map_image)
  world.process_data()
  world.process_enemies()

#########################
# GAME LOOP
#########################

  run = True
  while run:
  
    clock.tick(c.FPS)

  
    if game_over == False:
      # Verifie si le joueur a perdu
      if world.health <= 0:
        game_over = True
        game_outcome = -1 # Défaite
  
      # Verifie si le joueur a gagné
      if world.level > c.TOTAL_LEVELS:
        game_over = True
        game_outcome = 1 # Victoire
  
  
      #update groups
      enemy_group.update(world)
      turret_group.update(enemy_group, world)
  
      # Surligne la Tourelle selectionée
      if selected_turret:
        selected_turret.selected = True
  
  
  
    #########################
    # DRAWING SECTION
    #########################
  
    #draw level
    world.draw(screen)
  
    #draw groups
    enemy_group.draw(screen)
    for turrets in turret_group:
      turrets.draw(screen)
  
    display.display_data(screen, world)
  
    if game_over == False:
      # Bouton Retour Menu
      if buttons['cancel_menu_button'].draw(screen):
        load.button_sound.play()
        menu.run_menu()
  
      # Verifie si le Level a commencé
      if level_started == False:
        if buttons['begin_button'].draw(screen):
          load.button_sound.play()
          level_started = True

      else:
        # Acceleration
        world.game_speed = 1
        if buttons['fast_forward_button'].draw(screen):
          world.game_speed = 2
        # Spawn ennemis
        if pg.time.get_ticks() - last_enemy_spawn > c.SPAWN_COOLDOWN:
          if world.spawned_enemies < len(world.enemy_list):
            enemy_type = world.enemy_list[world.spawned_enemies]
            enemy = Enemy(enemy_type, world.waypoints, load.enemy_images)
            enemy_group.add(enemy)
            world.spawned_enemies += 1
            last_enemy_spawn = pg.time.get_ticks()
  
      # Verifie si la vague est terminée
      if world.check_level_complete() == True:
        world.money += c.LEVEL_COMPLETE_REWARD
        world.level += 1
        wave_number += 1  # Incrémentez la variable du nombre de vagues écoulées
        level_started = False
        last_enemy_spawn = pg.time.get_ticks()
        world.reset_level()
        world.process_enemies()
  
      if wave_number % 5 == 0 and wave_number > 0 and not boss_spawned:
        boss_image = pg.image.load("assets/images/enemies/boss.png")  # Chargez l'image du boss
        boss = Enemy("boss", world.waypoints, {"boss": boss_image})
        enemy_group.add(boss)
        last_enemy_spawn = pg.time.get_ticks()
        boss_spawned = True 
  
        
      # Bouton pour placer Tourelles
      display.draw_text(screen, str(c.BUY_COST), load.text_font, "grey100", c.SCREEN_HEIGHT + 215, 135)
      screen.blit(load.coin_image, (c.SCREEN_WIDTH + 260, 130))
      if buttons['turret_button'].draw(screen):
        load.button_sound.play()
        placing_turrets = True
      # Si tourelle en Cursor, montre le bouton Cancel
      if placing_turrets == True:
        # Curseur de Tourelle
        cursor_rect = load.cursor_turret.get_rect()
        cursor_pos = pg.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[0] <= c.SCREEN_WIDTH:
          screen.blit(load.cursor_turret, cursor_rect)
        if buttons['cancel_button'].draw(screen):
          load.button_sound.play()
          placing_turrets = False
      # Si une tourelle est selectionée
      if selected_turret:
        # Si la tourelle peut etre améliorée
        if selected_turret.upgrade_level < c.TURRET_LEVELS:
          # Montre le cout des Upgrade
          display.draw_text(screen, str(c.UPGRADE_COST), load.text_font, "grey100", c.SCREEN_WIDTH + 215, 195)
          screen.blit(load.coin_image, (c.SCREEN_WIDTH + 260, 190))
          if buttons['upgrade_button'].draw(screen):
            if world.money >= c.UPGRADE_COST:
              load.button_sound.play()
              selected_turret.upgrade()
              world.money -= c.UPGRADE_COST
    else:
      pg.draw.rect(display.screen, (50,50,50), (200, 200, 400, 200), border_radius = 30)
      if game_outcome == -1:
        display.draw_text("PERDU !", load.large_font, "grey0", 350, 230)
      elif game_outcome == 1:
          screen.fill(WHITE)
          display.draw_text(screen, "BRAVO !", load.large_font, BLACK, c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2)
          pg.display.flip()
  
      if buttons['restart_button'].draw(screen):
        load.button_sound.play()
        game_over = False
        level_started = False
        placing_turrets = False
        selected_turret = None
        last_enemy_spawn = pg.time.get_ticks()
  
        # Créer le monde
        world = World(load.world_data, load.map_image)
        world.process_data()
        world.process_enemies()
  
        # Vide les Groupes
        enemy_group.empty()
        turret_group.empty()
  
  
    #event handler
    for event in pg.event.get():
      # Ferme le programme
      if event.type == pg.QUIT:
        run = False
  
      #mouse click
      if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = pg.mouse.get_pos()
        # Verifie si la souris est sur la page
        if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
          # Deselectionne toutes les Tourelles
          selected_turret = None
          turret.clear_selection(turret_group)
          if placing_turrets == True:
            # Si assez d'argent
            if world.money >= c.BUY_COST:
              turret.create_turret(world, mouse_pos, turret_group)
          else:
            selected_turret = turret.select_turret(mouse_pos,turret_group)
  
    #update display
    pg.display.flip()