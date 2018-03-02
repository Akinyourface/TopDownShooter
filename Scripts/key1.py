from Globals import *


class Key1(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 16, 16, (255, 255, 255), "../Images/key1.png")
        GroupManager.camera_group.add(self)
