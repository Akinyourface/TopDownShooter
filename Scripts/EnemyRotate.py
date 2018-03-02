from Globals import *
from enemy_bullet import *
from enemyFollowDestroyed import *



class EnemyRotate(Actor):
    def __init__(self, startx, starty):
        super().__init__(startx, starty, 16, 16, (255, 255, 255), "../Images/enemy_follow.png")
        self.shootcount = 0
        self.shootmax = 50
        self.health = 100
        self.speed = 0
        GroupManager.camera_group.add(self)
        self.name = "Rotate"

    def _update(self, player):
        if self.health <= 0:
            corpse = EnemyFollowDestroyed(self.rect.x, self.rect.y, math.degrees(self.rotation))
            GroupManager.corpse_sprite.add(corpse)
            self.kill()
        self.rotation = math.atan2(self.rect.center[1]-player.rect.y, player.rect.x-self.rect.center[0])
        #self.image = pygame.transform.rotate(self.imageS, math.degrees(self.rotation))

        self.toPlayerX = player.rect.x - self.rect.x
        self.toPlayerY = player.rect.y - self.rect.y
        self.playerDis = int(math.sqrt(self.toPlayerX * self.toPlayerX + self.toPlayerY * self.toPlayerY))

        if self.playerDis <= 200:
            self.image = super().rot_center(self.imageS, math.degrees(self.rotation))
            #self.image = pygame.transform.rotate(self.imageS, math.degrees(self.rotation))
            if self.shootcount >= self.shootmax:
                eb = Enemybullet(self.rect.x, self.rect.y, 10, player)
                GroupManager.bullet_sprite.add(eb)
                eb.walls = GroupManager.wall_sprite
                self.shootcount = 0
            else:
                self.shootcount += 1
    def _Render_health(self, font, display):
        if self.health < 100:
            pygame.draw.rect(display, (255, 0, 0), (self.rect.x, self.rect.y - 20, self.health / 4, 5))
            #self.fontimage = font.render(str(self.health),1, (255, 255, 255))
            #display.blit(self.fontimage, (self.rect.x, self.rect.y - 15))
