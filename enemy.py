import pygame as pg
from pygame.math import Vector2
import math
import constants as c
from enemy_data import ENEMY_DATA

class Enemy(pg.sprite.Sprite):
  def __init__(self, enemy_type, waypoints, images):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.health = ENEMY_DATA.get(enemy_type)["health"]
        self.speed = ENEMY_DATA.get(enemy_type)["speed"]
        self.angle = 0
        self.images = images[enemy_type]
        self.image_index = 0  # Index de l'image actuelle de l'animation.
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.animation_speed = 0.2  # Vitesse de l'animation de marche.
        self.time_elapsed = 0



  def update(self, world,dt):
      self.move(world)
      self.rotate()
      self.check_alive(world)
      self.update_animation(dt)

  def move(self, world,):
    #define a target waypoint
    if self.target_waypoint < len(self.waypoints):
      self.target = Vector2(self.waypoints[self.target_waypoint])
      self.movement = self.target - self.pos
    else:
      #enemy has reached the end of the path
      self.kill()
      world.health -= 1
      world.missed_enemies += 1

    #calculate distance to target
    dist = self.movement.length()
    #check if remaining distance is greater than the enemy speed
    if dist >= (self.speed * world.game_speed):
      self.pos += self.movement.normalize() * (self.speed * world.game_speed)
    else:
      if dist != 0:
        self.pos += self.movement.normalize() * dist
      self.target_waypoint += 1

  def rotate(self):
    #calculate distance to next waypoint
    dist = self.target - self.pos
    #use distance to calculate angle
    self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
    #rotate image and update rectangle
    self.image = pg.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect()
    self.rect.center = self.pos

  def check_alive(self, world):
    if self.health <= 0:
      world.killed_enemies += 1
      world.money += c.KILL_REWARD
      self.kill()

def update_animation(self, dt):
        # Mettez à jour l'image de l'animation de marche en fonction du temps écoulé.
        self.time_elapsed += dt
        if self.time_elapsed >= self.animation_speed:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.time_elapsed = 0

