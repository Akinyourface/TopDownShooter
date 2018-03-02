from Globals import *

class levelExit(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 16, 16, (255, 0, 0), "../Images/levelExit.png")
        GroupManager.camera_group.add(self)

    def _update(self, tilemap):
    	self.player_collide = pygame.sprite.spritecollide(self, self.player, False)
    	for col in self.player_collide:
    		tilemap.unload_map()
