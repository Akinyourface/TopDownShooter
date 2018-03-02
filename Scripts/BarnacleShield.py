from Globals import *


class BarnacleShield(Actor):
    def __init__(self, startingx, startingy, health):
        super().__init__( startingx, startingy, 100, 100, (255, 255, 255), "../Images/BarnacleShield.png")
        self.image.set_colorkey((255, 255, 255))
        self.health = 500
        GroupManager.camera_group.add(self)

    def _update(self, player):
        self.bullet_collide = pygame.sprite.spritecollide(self, self.bullets, False)
        for col in self.bullet_collide:
            if self.health > 0:
                for ent in GroupManager.player_sprite:
                    self.health -= ent.playerInventory.getCurrentItem().damage
                    col.kill()
            else:
                self.kill()
