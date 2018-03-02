from Globals import *


class Gui:
    def __init__(self, x, y):
        self.elements = []
        for ent in GroupManager.player_sprite:
            self.elements.append(ent.playerInventory.listofItems)
    def update(self, player):
        #self.elements.append(player.playerInventory.listofItems)
        pass
