from Globals import *


class WeaponTileAssault(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 16, 16, (255, 255, 255), "../Images/WeaponTileAssault.png")
        GroupManager.camera_group.add(self)

    def update(self):
        self.player_collide = pygame.sprite.spritecollide(self, self.player, False)

        for col in self.player_collide:
            if len(col.playerInventory.listofItems) > 1:
                if col.assault.currentAmmo < col.assault.ammoCapacity:
                    col.assault.currentAmmo += 10
                    self.kill()
                else:
                    print("ammo is full")
            else:
                col.playerInventory.addToInventory(col.assault)
                self.kill()
