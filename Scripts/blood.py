from Globals import *
from random import randint

class BloodStain(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 16, 16, (0, 0, 0), "../Images/blood.png")
        self.rotation = randint(0, 360)
        self.image = pygame.transform.rotate(self.imageS, self.rotation)
        self.life = 50
        GroupManager.camera_group.add(self)
    def update(self):
        if self.life >= 0:
            self.life -= 1
        else:
            self.kill()
