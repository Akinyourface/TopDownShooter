from Globals import *
from BarnacleTenticle import *
from BarnacleShield import *

class Barnacle(Actor):
    def __init__(self, startingx, startingy):
        super().__init__(startingx, startingy, 16, 16, (255, 255, 255), "../Images/Barnacle.png")
        self.barnacles = [
            BarnacleTenticle(self.rect.x - 16, self.rect.y, self),
            BarnacleTenticle(self.rect.x, self.rect.y - 16, self),
            BarnacleTenticle(self.rect.x, self.rect.y + 16, self),
            BarnacleTenticle(self.rect.x + 16, self.rect.y, self)
        ]
        self.barnacleShields = BarnacleShield(self.rect.x - 50, self.rect.y - 50, 500)
        self.barnacleShields.bullets = GroupManager.player_bullet
        GroupManager.camera_group.add(self)
        self.barnacleGroup = pygame.sprite.Group()
        self.barnacleShield = pygame.sprite.Group()
        for ent in self.barnacles:
            self.barnacleGroup.add(ent)
            ent.bullets = GroupManager.player_bullet
        self.barnacleShield.add(self.barnacleShields)
        self.barnacleGroup.add(self.barnacleShield)
        self.health = 250

    def update(self):
        for ent in self.barnacleGroup:
            for entF in GroupManager.player_sprite:
                ent._update(entF)
                for ent in self.barnacleShield:
                    ent._update(entF)
        self.bullet_collide = pygame.sprite.spritecollide(self, self.bullets, False)
        for col in self.bullet_collide:
            if self.health > 0:
                for ent in GroupManager.player_sprite:
                    self.health -= ent.playerInventory.getCurrentItem().damage
                    col.kill()
            else:
                self.kill()



    def _draw(self, display):
        self.barnacleGroup.draw(display)
        self.barnacleShield.draw(display)
