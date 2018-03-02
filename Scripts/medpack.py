from Globals import *

class Medpack(Actor):
    def __init__(self, x, y, healtrate):
        super().__init__(x, y, 16, 16, (255, 255, 255), "../Images/MedPack.png")

    def update(self):
        self.player_collide = pygame.sprite.spritecollide(self, self.player, False)
        GroupManager.camera_group.add(self)

        for col in self.player_collide:
            if col.health < 100:
                col.health += 10
                self.kill()
            else:
                print("you have full health")
