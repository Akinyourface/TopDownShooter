from Globals import *


class WeaponTileRocket(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 16, 16, (255, 255, 255), "../Images/rocketInventory.png")
        GroupManager.camera_group.add(self)

    def update(self):
        self.player_collide = pygame.sprite.spritecollide(self, self.player, False)

        for col in self.player_collide:
            if len(col.playerInventory.listofItems) > 2:
                if col.rocket.currentAmmo < col.rocket.ammoCapacity:
                    col.rocket.currentAmmo += 3
                    self.kill()
                else:
                    print("ammo is full")
            else:
                col.playerInventory.addToInventory(col.rocket)
                self.kill()
