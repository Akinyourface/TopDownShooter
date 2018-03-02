from Globals import *
from Grass import *
from Wall import *
from Enemy_follow import *
from EnemyRotate import *
from tileFloor import *
from levelExit import *
from door1 import *
from key1 import *
from planet import *
from medpack import *
from Barnacle import *
from WeaponTileAssault import *
from WeaponTileRocket import *
from DestructableBlock import *
class TileMap:
    def __init__(self, filename = "../Levels/level1.txt"):
        self.filename = filename
        self.currentLevel = 0

        self.levels = [row.strip('\n') for row in open("../Levels/levels.txt" , 'r').readlines()]
        self.level = [row.strip('\n') for row in open(self.levels[0], 'r').readlines()]
        print(len(self.levels))

        self.levelWidth = len(self.level[0])
        self.levelHeight = len(self.level)
        #self.rect = pygame.Rect((self.levelWidth, self.levelHeight))
        self.blockWidth = 16
        self.localCamX = 0
        self.localCamY = 0

    def reload_map(self, display):
        self.level = []

        for ent in GroupManager.grass_sprite:
            ent.kill()
        for ent in GroupManager.wall_sprite:
            ent.kill()
        for ent in GroupManager.enemy_sprite:
            ent.kill()
        for ent in GroupManager.level_exit:
            ent.kill()
        for ent in GroupManager.player_sprite:
            ent.rect.x = 50
            ent.rect.y = 50
        for ent in GroupManager.healthpack_sprite:
            ent.kill()
        self.level = [row.strip('n') for row in open(self.filename, 'r').readlines()]
        self.draw_map(display)
    def unload_map(self):
        if self.currentLevel < len(self.levels) - 1:
            self.currentLevel += 1
            for ent in GroupManager.grass_sprite:
                ent.kill()
            for ent in GroupManager.wall_sprite:
                ent.kill()
            for ent in GroupManager.enemy_sprite:
                ent.kill()
            for ent in GroupManager.level_exit:
                ent.kill()
            for ent in GroupManager.blood_sprite:
                ent.kill()
            for ent in GroupManager.tile_Move:
                ent.kill()
            self.filename = self.levels[self.currentLevel]
            self.reload_map(2)
        else:
            print("end level")


    def draw_map(self, display):

        for x in range(self.levelWidth):
            for y in range(self.levelHeight):
                if self.level[y][x] == "0":
                    #print("it works")
                    wall = Wall(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.wall_sprite.add(wall)
                    GroupManager.all_sprite.add(wall)
                if self.level[y][x] == ".":
                    grass = Grass(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.grass_sprite.add(grass)
                    #GroupManager.all_sprite.add(grass)
                if self.level[y][x] == "1":
                    enemy = Enemyfollow(x * self.blockWidth, y * self.blockWidth)
                    enemy.walls = GroupManager.wall_sprite
                    enemy.player = GroupManager.player_sprite
                    GroupManager.enemy_sprite.add(enemy)
                    grass = Grass(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.grass_sprite.add(grass)
                if self.level[y][x] == "2":
                    enemy = EnemyRotate(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.enemy_sprite.add(enemy)
                    grass = Grass(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.grass_sprite.add(grass)
                if self.level[y][x] == "3":
                    floorTile = tileFloor(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.floor_sprite.add(floorTile)
                if self.level[y][x] == "4":
                    exit = levelExit(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.level_exit.add(exit)
                    exit.player = GroupManager.player_sprite
                if self.level[y][x] == "D":
                    door = Door1(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.door1_sprite.add(door)
                    GroupManager.wall_sprite.add(door)
                if self.level[y][x] == "A":
                    key = Key1(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.key1_sprite.add(key)
                if self.level[y][x] == "P":
                    planet = Planet(randint(0, 640), randint(0, 480), 0.25)
                    GroupManager.planet_sprite.add(planet)
                if self.level[y][x] == "5":
                    medpack = Medpack(x * self.blockWidth, y * self.blockWidth, 10)
                    GroupManager.healthpack_sprite.add(medpack)
                    medpack.player = GroupManager.player_sprite
                    grass = Grass(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.grass_sprite.add(grass)
                if self.level[y][x] == "B":
                    barnacle = Barnacle(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.barnacle_group.add(barnacle)
                    barnacle.walls = GroupManager.wall_sprite
                    barnacle.player = GroupManager.player_sprite
                    barnacle.bullets = GroupManager.player_bullet
                if self.level[y][x] == "R":
                    assault = WeaponTileAssault(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.weapon_group.add(assault)
                    assault.player = GroupManager.player_sprite
                if self.level[y][x] == "L":
                    rocket = WeaponTileRocket(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.weapon_group.add(rocket)
                    rocket.player = GroupManager.player_sprite
                if self.level[y][x] == "E":
                    Dblock = DestructableBlock(x * self.blockWidth, y * self.blockWidth)
                    #GroupManager.wall_sprite.add(Dblock)
                    GroupManager.all_sprite.add(Dblock)
                    GroupManager.destructable_block.add(Dblock)
                    Dblock.playerBullet = GroupManager.bullet_sprite
                    Dblock.playerCollide = GroupManager.player_sprite
