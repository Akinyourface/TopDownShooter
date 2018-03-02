from Globals import *
from player_bullet import *
from Camera import *
from inventory import *
from Simple_Pistol import *
from blood import *
from Assault_Rifle import *
from RocketLauncher import *
from Gui import *
from rocket_bullet import *



class Player(Actor):
    def __init__(self, startingx, startingy):
        super().__init__(startingx, startingy, 16, 16, (0, 0, 0), "../Images/player.png")
        self.dir = 0
        super().register_subclass("player")
        self.deltax = 0
        self.deltay = 0
        self.image.set_colorkey((255, 0, 255))
        self.playerspeed = 4
        self.health = 100
        self.stamina = 100
        self.playerInventory = Inventory()
        GroupManager.camera_group.add(self)


        self.pistol = SimplePistol()
        self.assault = AssaultRifle()
        self.rocket = RocketLauncher()
        self.playerInventory.addToInventory(self.pistol)

        #self.playerInventory.addToInventory(self.assault)
        #self.currentWeapon = self.playerInventory[0]
        print(self.playerInventory.listofItems)

    def _update_keypressed(self, event):

        if event.key == pygame.K_a:
            #player.dir = 1
            self.deltax = -self.playerspeed
        if event.key == pygame.K_d:
            #player.dir = 2
            self.deltax = self.playerspeed
        if event.key == pygame.K_w:
            #player.dir = 3
            self.deltay = -self.playerspeed
        if event.key == pygame.K_s:
            #player.dir = 4
            self.deltay = self.playerspeed
        if event.key == pygame.K_SPACE:
            if self.playerInventory.getCurrentItem().currentAmmo > 0:
                if self.playerInventory.getCurrentItem().name == "SimplePistol" or self.playerInventory.getCurrentItem().name == "AssaultRifle":
                    print(self.playerInventory.getCurrentItem().currentAmmo)
                    eb = playerBullet(self.rect.center[0], self.rect.center[1], 10, pygame.mouse.get_pos())
                    GroupManager.player_bullet.add(eb)
                    eb.walls = GroupManager.wall_sprite
                    eb.enemy = GroupManager.enemy_sprite
                    eb.Dblock = GroupManager.destructable_block
                    self.playerInventory.getCurrentItem().currentAmmo -= 1
                if self.playerInventory.getCurrentItem().name == "Rocket":
                    print(self.playerInventory.getCurrentItem().currentAmmo)
                    rb = playerRocketBullet(self.rect.center[0], self.rect.center[1], 10, pygame.mouse.get_pos())
            
                    groupManager.rocket_bullet.add(rb)
                    rb.walls = GroupManager.wall_sprite
                    rb.enemy = GroupManager.enemy_sprite
                    self.playerInventory.getCurrentItem().currentAmmo -= 1
                    print("test")
            else:
                print("You have no ammo")
        if event.key == pygame.K_1:
            self.playerInventory.setCurrentItem("Pistol")
            print("Switched to pistol")
        if event.key == pygame.K_2:
            if len(self.playerInventory.listofItems) > 1:
                self.playerInventory.setCurrentItem("Assault")
                print("Switched to Assault Rifle")
            else:
                print("you do not have this weapon")
        if event.key == pygame.K_3:
            if len(self.playerInventory.listofItems) > 2:
                self.playerInventory.setCurrentItem("Rocket")
                print("Switched to Rocket Launcher")
            else:
                print("You do not have this weapon")



    def _update_keyup(self, event):

        if event.key == pygame.K_a:
            self.deltax = 0
        if event.key == pygame.K_d:
            self.deltax = 0
        if event.key == pygame.K_w:
            self.deltay = 0
        if event.key == pygame.K_s:
            self.deltay = 0
        if pygame.key.get_mods() & KMOD_SHIFT:
            Camera.CameraEntSpeed = 4
            self.playerspeed = 4

    def update(self):
       #super().actor_update()
        #self.image = pygame.transform.scale(self.image, (self.rect.width * Camera.CameraZoom, self.rect.height * Camera.CameraZoom))
        #self.rect = self.image.get_rect()
        self.rect.x += self.deltax
        self.block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        self.rect.y += self.deltay
        for block in self.block_hit_list:
            if self.deltax > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in self.block_hit_list:
            if self.deltay > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        self.bullet_hit_list = pygame.sprite.spritecollide(self, self.bullet, True)
        self.enemy_hit_list = pygame.sprite.spritecollide(self, self.enemy, False)
        #self.weapon_hit_list = pygame.sprite.spritecollide(self, self.weapon, true)


        for col in self.enemy_hit_list:
            if self.health > 0:
                blood = BloodStain(self.rect.x, self.rect.y)
                GroupManager.blood_sprite.add(blood)
                self.health -= 10
                print("you were hit!")
            else:
                self.kill()


        for col in self.bullet_hit_list:
            if self.health > 0:
                blood = BloodStain(self.rect.x, self.rect.y)
                GroupManager.blood_sprite.add(blood)
                self.health -= 10
                print("you were hit!")
            else:
                self.kill()



    def update_rotation(self, mousePos):

        self.rotation = math.atan2(mousePos[0] - self.rect.center[0] + 16 / 2, mousePos[1] - self.rect.center[1] + 16 / 2)
        #self.image = pygame.transform.rotate(self.imageS, math.degrees(self.rotation))

        self.image = super().rot_center(self.imageS, math.degrees(self.rotation))
    def Render_health(self, font, display):
        pygame.draw.rect(display, (255, 0, 0), (self.rect.x - 16 / 2, self.rect.y - 15, self.health / 4, 5))
        self.render_inventory(display)
    def init_inventory(self):
        self.visualInventory = Gui(100, 100)
    def render_inventory(self, display):
        display.blit(self.playerInventory.getCurrentItem().image, (2, 2))
