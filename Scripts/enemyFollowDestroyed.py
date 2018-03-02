from Globals import *


class EnemyFollowDestroyed(Actor):
    def __init__(self, startingx, startingy, rotation):
        super().__init__(startingx, startingy, 16, 16, (255, 255, 255), "../Images/enemy_follow_destroyed.png")
        self.life = 100
        self.image = super().rot_center(self.imageS, rotation)
        GroupManager.camera_group.add(self)
    def update(self):
        if self.life >= 0:
            self.life -= 1
        else:
            self.kill()
