from Globals import *
from WeaponTileAssault import *
from WeaponTileRocket import *
import random

class DestructableBlock(Actor):
    def __init__(self, startingx, startingy): #should i have it where the health is init as the block is init?
        super().__init__(startingx, startingy)
        self.health = 100
        GroupManager.camera_group.add(self)
        GroupManager.wall_sprite.add(self)

    def update(self):
        if self.health < 0:
            chance = random.randint(1, 100)
            if chance < 25:
                assault = WeaponTileAssault(self.rect.x, self.rect.y)
                GroupManager.weapon_group.add(assault)
                assault.player = GroupManager.player_sprite
                

            self.kill()
