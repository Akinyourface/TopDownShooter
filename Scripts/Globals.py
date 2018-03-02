import pygame
from pygame.locals import *
import math
TILE_WIDTH = 16
TILE_HEIGHT = 16
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
DEBUG = True

class GroupManager:
    all_sprite = pygame.sprite.Group()
    player_sprite = pygame.sprite.Group()
    wall_sprite = pygame.sprite.Group()
    grass_sprite = pygame.sprite.Group()
    enemy_sprite = pygame.sprite.Group()
    floor_sprite = pygame.sprite.Group()
    planet_sprite = pygame.sprite.Group()
    bullet_sprite = pygame.sprite.Group()
    tile_Move = pygame.sprite.Group()
    player_bullet = pygame.sprite.Group()
    blood_sprite = pygame.sprite.Group()
    level_exit = pygame.sprite.Group()
    door1_sprite = pygame.sprite.Group()
    key1_sprite = pygame.sprite.Group()
    scrolling_background = pygame.sprite.Group()
    healthpack_sprite = pygame.sprite.Group()
    corpse_sprite = pygame.sprite.Group()
    camera_group = pygame.sprite.Group()
    barnacle_group = pygame.sprite.Group()
    weapon_group = pygame.sprite.Group() #controls the many weapons in the game
    destructable_block = pygame.sprite.Group()
    rocket_bullet = pygame.sprite.Group()

class Actor(pygame.sprite.Sprite):
    totalActorCount = []
    def __init__(self, x, y, width = TILE_WIDTH, height = TILE_HEIGHT, color = (255, 255, 255), filename = "../Images/default.png", doRender = True):
        super().__init__()
        if doRender == True:
            self.image = pygame.Surface([width, height])
            #self.image.set_colorkey((255, 0, 255))
            #self.image.fill(color)
            self.imageS = pygame.image.load(filename)
            #self.imageS.set_colorkey((255, 0, 255))

            #self.image.fill(color)

            self.rect = self.image.get_rect()

            self.image.blit(self.imageS, (self.rect.x, self.rect.y))

            #self.imageS.set_colorkey((255, 0, 255))
            #self.imageS.set_colorkey((255, 0, 255))
            self.rect.x = x
            self.rect.y = y
            self.rotation = 0
    def register_subclass(self, name):
        print("Registered " + name +  " as a subclass of Actor")
        self.totalActorCount.append(name)
    def actor_update(self):
        if self.rect.x < 40:
            self.doRender = false
            print(self.doRender)
    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
