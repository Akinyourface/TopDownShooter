from Globals import *


class Corpse(Actor):
    def __init__(self, startingx, startingy):
        super().__init__(startingx, startingy, 16, 16, (255, 255, 255), "../Images/Corpse.png")
        self.life = 100
        GroupManager.camera_group.add(self)
    def update(self):
        if self.life >= 0:
            self.life -= 1
        else:
            self.kill()
