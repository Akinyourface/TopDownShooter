from Globals import *
import math
from enemy_bullet import *
from corpse import *
class BarnacleTenticle(Actor):
    def __init__(self, startingx, startingy, parent):
        self.parent = parent
        super().__init__(startingx, startingy, 16, 16, (255, 255, 255), "../Images/BarnacleTenticle.png")
        GroupManager.camera_group.add(self)
        self.health = 250
        self.shootcount = 0
        self.shootmax = 30

    def _update(self, player):
        #self.rect.x = self.parent.rect.x
        if self.health <= 0:
            corpse = Corpse(self.rect.x, self.rect.y)
            GroupManager.corpse_sprite.add(corpse)
            self.kill()
        self.rotation = math.atan2(self.rect.center[1]-player.rect.y, player.rect.x-self.rect.center[0])
        #self.image = pygame.transform.rotate(self.imageS, math.degrees(self.rotation))
        self.bullet_collide = pygame.sprite.spritecollide(self, self.bullets, False)
        for col in self.bullet_collide:
            if self.health > 0:
                for ent in GroupManager.player_sprite:
                    self.health -= ent.playerInventory.getCurrentItem().damage
                    col.kill()
            else:
                self.kill()
        self.toPlayerX = player.rect.x - self.rect.x
        self.toPlayerY = player.rect.y - self.rect.y
        self.playerDis = int(math.sqrt(self.toPlayerX * self.toPlayerX + self.toPlayerY * self.toPlayerY))

        if self.playerDis <= 200:
            self.image = super().rot_center(self.imageS, math.degrees(self.rotation))
            #self.image = pygame.transform.rotate(self.imageS, math.degrees(self.rotation))
            if self.shootcount >= self.shootmax:
                eb = Enemybullet(self.rect.x, self.rect.y, 10, player)
                GroupManager.bullet_sprite.add(eb)
                eb.walls = GroupManager.wall_sprite
                self.shootcount = 0
            else:
                self.shootcount += 1
